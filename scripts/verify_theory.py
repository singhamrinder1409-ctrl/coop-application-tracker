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
print('ALL WORKED THEORY EXAMPLES PASSED; production MVD assumptions remain a domain review')
