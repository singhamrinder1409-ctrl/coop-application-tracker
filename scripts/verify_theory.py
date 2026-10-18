#!/usr/bin/env python3
"""Check the worked examples in NORMALIZATION.md, independently of live SQL data."""
from itertools import combinations
from design import closure

def subsets(attrs):
    return [set(s) for n in range(len(attrs)+1) for s in combinations(sorted(attrs),n)]

def equivalent(attrs,left,right):
    return all(closure(s,left)==closure(s,right) for s in subsets(attrs))

def keys(attrs,fds):
    result=[]
    for s in subsets(attrs):
        if closure(s,fds)==set(attrs) and not any(k<=s for k in result): result.append(s)
    return result

original=[(('A',),'S'),(('A',),'N'),(('A',),'P'),(('S',),'N'),(('A','P'),'S')]
minimal=[(('A',),'S'),(('A',),'P'),(('S',),'N')]
assert equivalent('ASNP',original,minimal)
for i,(lhs,rhs) in enumerate(minimal):
    assert rhs not in closure(lhs,minimal[:i]+minimal[i+1:])
    for a in lhs: assert rhs not in closure(set(lhs)-{a},minimal)
print('PASS minimal basis preserves every closure and has no redundant FD or LHS attribute')
projected=[(('A',),'N'),(('A',),'P')]
for s in subsets('ANP'): assert closure(s,minimal)&set('ANP') == closure(s,projected)
print('PASS projected basis matches all original closures restricted to A,N,P')
assert closure({'S'},minimal)>={'S','N'}
assert equivalent('ASNP',minimal,[(('A',),'S'),(('A',),'P'),(('S',),'N')])
print('PASS Flat decomposition is lossless and preserves the original FD basis')
resume_fds=[(('A',),'R'),(('A',),'S'),(('R',),'S')]
assert closure({'R'},resume_fds)>={'R','S'}
assert equivalent('ARS',resume_fds,[(('A',),'R'),(('R',),'S')])
print('PASS assigned-resume decomposition is lossless and dependency-preserving')
allocation=[(('S','P'),'M'),(('M',),'P')]
assert {frozenset(k) for k in keys('SPM',allocation)}=={frozenset('SP'),frozenset('SM')}
prime=set().union(*keys('SPM',allocation))
assert all(closure(lhs,allocation)==set('SPM') or rhs in prime for lhs,rhs in allocation)
assert closure({'M'},allocation)!=set('SPM') and 'P' in closure({'M'},allocation)
print('PASS Allocation is 3NF but violates BCNF, with both candidate keys verified')
# Both projected relations satisfy their local constraints, but their join
# permits one (student,project) pair to have two mentors.
mentor_project={('m1','p1'),('m2','p1')}; student_mentor={('s1','m1'),('s1','m2')}
joined={(s,p,m) for s,m in student_mentor for m2,p in mentor_project if m==m2}
assert len({m for s,p,m in joined if (s,p)==('s1','p1')})==2
print('PASS BCNF projection counterexample demonstrates lost local SP -> M enforcement')
preferences={('s1',skill,city) for skill in ('SQL','Python') for city in ('Victoria','Vancouver')}
skills={(s,k) for s,k,c in preferences}; cities={(s,c) for s,k,c in preferences}
reconstructed={(s,k,c) for s,k in skills for s2,c in cities if s==s2}
assert reconstructed==preferences and len(reconstructed)==4
incomplete=preferences-{('s1','SQL','Victoria')}
assert incomplete!=reconstructed
print('PASS 4NF independent-value decomposition reconstructs exactly four rows; missing combination disproves MVD')

# Full 3NF synthesis, including the mandatory key-relation step (lecture 23).
attrs=set('ASPNQT')  # application, student, posting, name, note, note text
fds=[(('A',),'S'),(('A',),'P'),(('S',),'N'),(('Q',),'T')]
assert keys(attrs,fds)==[set('AQ')]
relations=[set(lhs)|{rhs} for lhs,rhs in fds]
assert not any(closure(r,fds)==attrs for r in relations)
relations.append(set('AQ'))
projected=[]
for relation in relations:
    rfds=[(tuple(sorted(x)),y) for x in subsets(relation) for y in closure(x,fds)&relation-x]
    projected.extend(rfds)
    rkeys=keys(relation,rfds);rprime=set().union(*rkeys)
    for x in subsets(relation):
        for y in closure(x,rfds)-x:
            assert closure(x,rfds)==relation or y in rprime,(relation,x,y,'3NF violation')
assert equivalent(attrs,fds,projected)
assert any(closure(r,fds)==attrs for r in relations)
print('PASS full 3NF synthesis: AS, AP, SN, QT, added key relation AQ; all projected relations in 3NF and all FDs preserved')
# A legal project-shaped instance reconstructs exactly from the five projections.
columns=list('ASPNQT')
flat={('a1','s1','p1','n1','q1','t1'),('a1','s1','p1','n1','q2','t2'),('a2','s1','p2','n1','q2','t2')}
joined=[{}]
for relation in relations:
    names=sorted(relation)
    projection={tuple(row[columns.index(k)] for k in names) for row in flat}
    new=[]
    for partial in joined:
        for values in projection:
            record=dict(zip(names,values))
            if all(partial[k]==record[k] for k in partial.keys()&record.keys()):new.append(partial|record)
    joined=new
assert {tuple(record[c] for c in columns) for record in joined}==flat
print('PASS synthesized key relation supports exact reconstruction of the application-note example')

# Formal tuple-swap definition, not an FD closure approximation to MVDs.
def holds_mvd(rows,lhs,rhs):
    for t in rows:
        for u in rows:
            if any(t[i]!=u[i] for i in lhs):continue
            v=tuple(t[i] if i in lhs|rhs else u[i] for i in range(len(t)))
            if v not in rows:return False
    return True
assert holds_mvd(preferences,{0},{1}) and holds_mvd(preferences,{0},{2})
assert not holds_mvd(incomplete,{0},{1})
print('PASS formal MVD tuple-swap test, complementarity and missing-combination rejection')
correlated={('a',b,c,d) for b,c in [('b1','c1'),('b2','c2')] for d in ['d1','d2']}
assert holds_mvd(correlated,{0},{1,2}) and not holds_mvd(correlated,{0},{1})
assert holds_mvd(correlated,{0},{0}) and holds_mvd(correlated,{0},{1,2,3})
assert holds_mvd({('a','b','c1'),('a','b','c2')},{0},{1})
print('PASS MVDs cannot use the FD splitting rule; both trivial cases and FD-implied MVD tested')
# The corrected lecture's theatre example has two keys, not just one.
cinema=[(('H',),'C'),(('C','T'),'H')]
assert {frozenset(k) for k in keys('CHT',cinema)}=={frozenset('CT'),frozenset('HT')}
print('PASS corrected 3NF lecture: both cinema keys verified despite inconsistent 4NF review slide')
print('ALL WORKED THEORY EXAMPLES PASSED (including extended course checks); production MVD assumptions remain a domain review')
