#!/usr/bin/env python3
"""Generate complete ERD/schema and check keys, minimal bases, and BCNF.
FDs here are declared domain assumptions, not facts inferred from sample rows.
"""
from pathlib import Path
import re, itertools, html
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'schema.sql').read_text()
tables={}
for name, body in re.findall(r'CREATE TABLE (\w+) \((.*?)\n\);',text,re.S):
    cols=[]; pk=[]; nullable={}
    for line in body.splitlines():
        m=re.match(r'\s+(\w+)\s+(INT|VARCHAR\(\d+\)|TEXT|BOOLEAN|DATE(?:TIME)?|DECIMAL\(\d+,\d+\)|ENUM\([^\n]+?\))(?=\s|,|$)(.*)',line)
        if m:
            col,typ,tail=m.groups(); cols.append((col,typ)); nullable[col]=not ('NOT NULL' in tail or 'PRIMARY KEY' in tail)
            if 'PRIMARY KEY' in tail: pk.append(col)
    unique=[tuple(x.strip() for x in group.split(',')) for group in re.findall(r'UNIQUE \(([^)]+)\)',body)]
    keys=[tuple(pk)]+[u for u in unique if all(not nullable[a] for a in u)]
    tables[name]={'cols':cols,'keys':keys,'unique':unique,'nullable':nullable,'body':body}

def closure(x,fds):
    c=set(x)
    while True:
        n=c|{b for a,b in fds if set(a)<=c}
        if n==c:return c
        c=n

def basis(t):
    pk=t['keys'][0]; attrs=[a for a,_ in t['cols']]
    return [(pk,a) for a in attrs if a not in pk]+[(k,pk[0]) for k in t['keys'][1:]]

def check():
    for name,t in tables.items():
        attrs=set(a for a,_ in t['cols']); fds=basis(t)
        for i,(x,y) in enumerate(fds):
            assert y not in closure(x,fds[:i]+fds[i+1:]),(name,'redundant FD',x,y)
            for a in x: assert y not in closure(set(x)-{a},fds),(name,'extraneous',a)
        found=[]
        for size in range(1,len(attrs)+1):
            for x in itertools.combinations(sorted(attrs),size):
                if any(set(k)<=set(x) for k in found):continue
                c=closure(x,fds)
                if c==attrs:found.append(x)
                else:assert c==set(x),(name,'BCNF violation',x,c-set(x))
        assert {frozenset(k) for k in found}=={frozenset(k) for k in t['keys']}
        print('PASS',name,': minimal singleton-RHS basis;',len(found),'candidate key(s); BCNF under declared FDs')
    # Projection example: A->S, S->N, A->P. Project onto (A,N,P).
    assert closure({'A'},[(('A',),'S'),(('S',),'N'),(('A',),'P')]) >= {'A','N','P'}
    assert closure({'S'},[(('A',),'S'),(('S',),'N'),(('A',),'P')]) >= {'S','N'}
    for name,t in tables.items():
        for attr,_ in t['cols']:
            assert attr in (ROOT/'ERD.svg').read_text() and attr in (ROOT/'ERD.md').read_text(),(name,attr,'missing ERD attribute')
    print('PASS complete ERD attribute coverage; projected A -> N; lossless intersection S -> (S,N)')
    print('NOTE: finite checks validate the declared FD model, not completeness of domain assumptions or 4NF.')

def generate():
    md=['# Relational schema - Sprint 1','', 'Generated from `schema.sql` by `python3 scripts/design.py --generate`. All attributes are shown. Optional means SQL NULL is allowed.','']
    er=['# Complete ERD - Sprint 1','','Crow\'s-foot notation replaces the incomplete kick-off Chen diagram. Every SQL attribute appears below and in `ERD.svg`; the Mermaid source and relational schema also show SQL types. `PK` is the primary key, `FK` a reference, and `UK` a non-null alternate key component. See `RELATIONAL_SCHEMA.md` for nullable UNIQUE rules.','','```mermaid','erDiagram']
    for name,t in tables.items():
        md += ['## '+name,'','| Attribute | SQL type | Optional |','| --- | --- | --- |']
        for a,typ in t['cols']:md.append(f"| {a} | {typ} | {'yes' if t['nullable'][a] else 'no'} |")
        md+=['','Primary key: `'+', '.join(t['keys'][0])+'`.','Non-null candidate keys: '+ '; '.join('`'+', '.join(k)+'`' for k in t['keys'])+'.','']
        for u in t['unique']:md+=['SQL UNIQUE: `'+', '.join(u)+'`'+(' (nullable: not an unconditional classical candidate key).' if any(t['nullable'][a] for a in u) else '.'),'']
        for a,target,b in re.findall(r'FOREIGN KEY \((\w+)\) REFERENCES (\w+)\((\w+)\)',t['body']):md+=['Foreign key: `'+a+'` -> `'+target+'.'+b+'` (default RESTRICT/NO ACTION).','']
        er+=['    '+name+' {']
        fk=set(re.findall(r'FOREIGN KEY \((\w+)\)',t['body']))
        for a,typ in t['cols']:
            flags=[]
            if a in t['keys'][0]:flags+=['PK']
            if a in fk:flags+=['FK']
            if any(a in k for k in t['keys'][1:]):flags+=['UK']
            er+=['        '+re.sub(r'[^a-zA-Z0-9_]','_',typ)+' '+a+(' '+','.join(flags) if flags else '')]
        er+=['    }']
    rels=[('Employer','JobPosting','posts','many'),('Student','ResumeVersion','owns','many'),('Student','Application','submits','many'),('JobPosting','Application','receives','many'),('ApplicationStatus','Application','classifies','many'),('Application','Interview','has','many'),('Application','Offer','receives','one'),('Application','ApplicationResume','selects','one'),('ResumeVersion','ApplicationResume','used_by','many')]
    for a,b,label,card in rels:er+=['    '+a+' ||--'+('o{' if card=='many' else 'o|')+' '+b+' : '+label]
    er+=['```','','Every child has exactly one parent for each listed reference; each parent has zero or many children, except Offer and ApplicationResume (zero or one). An application without ApplicationResume has no selected resume. Ownership consistency also requires the triggers described in `docs/CONSTRAINTS.md`.','','![Complete ERD](ERD.svg)']
    (ROOT/'RELATIONAL_SCHEMA.md').write_text('\n'.join(md).rstrip()+'\n');(ROOT/'ERD.md').write_text('\n'.join(er)+'\n')
    # Render all attributes in readable entity cards; labelled relationship panel
    # keeps multiplicities explicit without crossing lines through attributes.
    w=1320; rowh=450; h=3*rowh+580
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">','<rect width="100%" height="100%" fill="#f4f7fb"/>','<style>text{font-family:ui-monospace,monospace;fill:#172a42} .title{font-family:Arial;font-weight:bold}</style>','<text x="28" y="36" font-size="25" class="title">Co-op Application Tracker · Complete relational ERD</text>','<text x="28" y="62" font-size="14">Every attribute shown · PK primary key · FK foreign key · ? nullable · relationship cardinalities below</text>']
    for i,(name,t) in enumerate(tables.items()):
        x=24+(i%3)*432;y=88+(i//3)*rowh
        out += [f'<rect x="{x}" y="{y}" width="408" height="424" rx="10" fill="white" stroke="#bccbdb"/>',f'<text x="{x+14}" y="{y+30}" font-size="19" class="title">{name}</text>']
        fk=set(re.findall(r'FOREIGN KEY \((\w+)\)',t['body']))
        for j,(a,typ) in enumerate(t['cols']):
            flags=('PK ' if a in t['keys'][0] else '')+('FK ' if a in fk else '')+('?' if t['nullable'][a] else '')
            out += [f'<text x="{x+14}" y="{y+60+j*25}" font-size="13">{html.escape(a)} {flags}</text>']
        out += [f'<text x="{x+14}" y="{y+401}" font-size="11">Keys: {html.escape("; ".join(" + ".join(k) for k in t["keys"]))}</text>']
    y=3*rowh+100
    out += [f'<text x="28" y="{y}" font-size="20" class="title">Relationship graph · each child references exactly one parent</text>', f'<text x="28" y="{y+25}" font-size="13">1 at parent end; 0..* or 0..1 at child end. Attributes for each node appear above.</text>']
    nodes={'Student':(150,y+90),'ApplicationStatus':(640,y+90),'Employer':(1130,y+90),
           'ResumeVersion':(150,y+230),'Application':(640,y+230),'JobPosting':(1130,y+230),
           'ApplicationResume':(150,y+420),'Interview':(640,y+420),'Offer':(1130,y+420)}
    for a,b,label,card in rels:
        ax,ay=nodes[a];bx,by=nodes[b]
        dx=bx-ax;dy=by-ay
        # Intersect a line with each rectangular node boundary.
        k=min(112/abs(dx) if dx else 100,24/abs(dy) if dy else 100)
        x1=ax+dx*k;y1=ay+dy*k;x2=bx-dx*k;y2=by-dy*k
        out += [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4b6d93" stroke-width="2"/>']
        for frac,lab in [(0.15,'1'),(0.50,label),(0.85,'0..*' if card=='many' else '0..1')]:
            xx=x1+(x2-x1)*frac; yy=y1+(y2-y1)*frac-6
            out += [f'<text x="{xx}" y="{yy}" text-anchor="middle" font-size="12" style="paint-order:stroke;stroke:#f4f7fb;stroke-width:5;stroke-linejoin:round">{lab}</text>']
    for name,(x,y) in nodes.items():
        out += [f'<rect x="{x-112}" y="{y-24}" width="224" height="48" rx="7" fill="white" stroke="#7795b5"/>',f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="15" class="title">{name}</text>']
    out+=['</svg>'];(ROOT/'ERD.svg').write_text('\n'.join(out))

if __name__=='__main__':
    if '--generate' in __import__('sys').argv:generate()
    check()
