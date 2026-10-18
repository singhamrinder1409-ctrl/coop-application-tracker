# Functional dependencies and normalization - Sprint 1

## Domain assumptions and SQL NULL

FDs describe all legal states, not patterns observed in the seed. Each ID identifies one fact; student usernames and status names are stable unique identifiers; a student has at most one application per posting and one resume per version number; each application has at most one interview per round and one offer. Names, cities, programs, wages and URLs shared across records imply no additional dependencies. In particular, city does not determine province, employer name alone does not identify an employer, and a posting title does not identify a posting.

For classical FD analysis, NULL denotes an optional fact outside the ordinary value model. We do **not** treat nullable SQL UNIQUE columns as unconditional candidate keys: Student.email, JobPosting.posting_url, and Employer(employer_name, website) permit multiple NULLs. On the subset with supplied non-NULL values, their uniqueness still applies. Our BCNF claim is relative to the declared domain dependencies, with optional attributes treated as single optional values; it is not a proof about every possible SQL NULL interpretation.

## Complete bases and table-by-table checks

For each row below, let `P` be the primary key and `N` every other attribute listed in `RELATIONAL_SCHEMA.md`. The notation `P -> each N` means one singleton-right-hand-side FD per non-key attribute, not one multivalued FD. Add exactly the listed alternate-key-to-P dependencies. This defines the complete FD model for each relation and a minimal basis for it.

| Relation | P | Additional basis FDs | All candidate keys | BCNF decision |
| --- | --- | --- | --- | --- |
| Student | student_id | username -> student_id | {student_id}, {username} | Both determinants are keys |
| Employer | employer_id | none | {employer_id} | Only ID determines other attributes |
| JobPosting | posting_id | none | {posting_id} | Only ID determines other attributes |
| ApplicationStatus | status_id | status_name -> status_id | {status_id}, {status_name} | Both determinants are keys |
| ResumeVersion | resume_id | student_id, version_number -> resume_id | {resume_id}, {student_id, version_number} | Both determinants are keys |
| Application | application_id | student_id, posting_id -> application_id | {application_id}, {student_id, posting_id} | Both determinants are keys |
| Interview | interview_id | application_id, interview_round -> interview_id | {interview_id}, {application_id, interview_round} | Both determinants are keys |
| Offer | offer_id | application_id -> offer_id | {offer_id}, {application_id} | Both determinants are keys |
| ApplicationResume | application_id | none | {application_id} | application_id -> resume_id; resume_id is reusable |

Key closures reach every attribute. For example, `{student_id, version_number}+` first reaches resume_id, then resume_label, created_on and file_name. Neither student_id alone nor version_number alone reaches resume_id. In Application, student_id and posting_id separately are not keys. In Offer, application_id reaches offer_id and then every offer attribute.

Minimality: each RHS is one attribute; deleting a key component destroys its ability to identify the record; removing any listed FD makes that RHS unreachable from its LHS. `scripts/design.py` tests each deletion and each LHS component. It also enumerates subsets of every relation, computes closures, checks all candidate keys, and rejects any non-key determinant with a nontrivial closure. Thus the BCNF decision checks implied dependencies too. This verifies the declared model, not whether our domain assumptions are complete.

## FDs in the ERD

An entity identifier determines its attributes. A many-to-one relationship gives a child-to-parent FD: posting_id -> employer_id; application_id -> student_id, posting_id, status_id; resume_id -> student_id; interview_id -> application_id. At-most-one offer gives application_id -> offer_id in Offer. Zero-or-one selected resume gives application_id -> resume_id in ApplicationResume. The reverse resume_id -> application_id does not hold: a student may reuse a resume. Multiplicity gives these dependencies; FDs alone cannot assert that the referenced parent exists, which requires foreign keys.

## The resume dependency and a lossless BCNF decomposition

Consider an assigned-resume fragment `R(A, S, R)` where A is application_id, S student_id, and R resume_id (using R for the attribute only in this paragraph). The domain gives A -> S,R and R -> S, because each resume has exactly one owner. A is the key; R is not a key because the same resume may serve several applications. R -> S violates BCNF. A composite FK enforcing ownership in the original Application table would enforce consistency but would not remove that dependency.

Decompose the fragment into `Assigned(A,R)` and `ResumeOwner(R,S)`. Their intersection is {R}; R -> ResumeOwner, so the decomposition is lossless. Both dependencies are preserved through these relations: A -> R and R -> S imply A -> S. ResumeOwner is already represented by ResumeVersion; Assigned is ApplicationResume. The full Application also retains student_id because saved applications without a resume still need an owner. That produces a cross-relation consistency rule: Application.student_id must equal ResumeVersion.student_id for each assignment. Triggers enforce this rule on insert/update, and owner IDs are immutable. A missing assignment represents an optional resume, instead of introducing a NULL resume determinant in Application.

## Minimal basis and FD projection worked example

For `Flat(A,S,N,P)` (application, student, student name, posting), start with
`F = { A -> S,N,P; S -> N; A,P -> S }`.
Split RHS: A->S, A->N, A->P, S->N, AP->S. P is extraneous in AP->S because A->S already holds. Remove the duplicate A->S, then remove A->N because A->S and S->N imply it. A minimal basis is `{A->S, A->P, S->N}`. No remaining FD or LHS attribute can be removed.

Project onto T(A,N,P): compute closures under the original basis, then intersect with T. A+ = {A,S,N,P}, so the projected basis is `{A->N, A->P}`. Simply retaining FDs whose symbols occur in T would miss A->N. Project onto U(S,N): basis `{S->N}`. The decomposition of Flat into V(A,S,P) and U(S,N) is lossless because their intersection S determines U; it preserves A->S, A->P, S->N. V and U are BCNF.

## 3NF: why it differs from BCNF

3NF permits X -> a if X is a superkey **or** a is prime (belongs to some candidate key); BCNF permits only the superkey condition for a nontrivial FD. All nine project tables satisfy BCNF under the model, so also 3NF.

A teaching example (not a production table) is `Allocation(Student, Project, Mentor)` with `{Student,Project}->Mentor` and `Mentor->Project`. Candidate keys are {Student,Project} and {Student,Mentor}. Mentor is not a superkey, so Mentor->Project violates BCNF; Project is prime, so it satisfies 3NF. Decomposing into MentorProject(Mentor,Project) and StudentMentor(Student,Mentor) is lossless (intersection Mentor determines MentorProject) but loses local enforcement of Student,Project->Mentor. A 3NF synthesis can retain Allocation to preserve that dependency. This is the dependency-preservation versus BCNF tradeoff; the project does not need that compromise for its declared FD model.

## 4NF and independent multivalued facts

BCNF alone does not imply 4NF. Consider a proposed `StudentPreference(student_id, skill, preferred_city)` where skills and preferred cities vary independently. Then student_id ->> skill and student_id ->> preferred_city are nontrivial MVDs, but student_id is not a superkey. For skills {SQL,Python} and cities {Victoria,Vancouver}, the representation needs four combinations. Split into StudentSkill(student_id,skill) and StudentPreferredCity(student_id,preferred_city). Their natural join reconstructs exactly those four combinations under the independence assumption: a lossless 4NF decomposition. A missing combination in the original would mean the claimed independence/MVD was false.

The production model stores single values for program, location, file_name and other scalar attributes; interviews and resume versions already live in separate relations rather than an independent resume/interview cross-product. We have identified no further independent nontrivial MVDs with a non-superkey determinant. Under that explicit assumption the nine relations satisfy 4NF; this is a domain review, not something the FD-only verifier proves. Multiple skills/cities are not secretly stored as comma-separated lists. If such requirements arise, add separate relations and revisit MVDs.
