# Constraints, relational algebra, and advanced design decisions

Let A=Application, S=Student, J=JobPosting, R=ResumeVersion, AR=ApplicationResume, I=Interview, O=Offer, T=ApplicationStatus. Set difference must be empty for each inclusion constraint. Aliases qualify equal column names in joins. In the ownership rule, join only on application_id and resume_id; a natural join that also equates student_id would incorrectly hide ownership violations. Comparisons on optional values below apply only to non-NULL supplied values.

| Rule | Formal constraint | Implementation and evidence |
| --- | --- | --- |
| Every application has a student | π_student_id(A) − π_student_id(S) = ∅ | NOT NULL FK; orphan insert rejected |
| Every application has a posting | π_posting_id(A) − π_posting_id(J) = ∅ | NOT NULL FK |
| Dates ordered | σ_(application_deadline < date_posted)(J) = ∅ | CHECK; reversed date rejected |
| Unique application | For a,b ∈ A, a.student_id=b.student_id ∧ a.posting_id=b.posting_id ⇒ a.application_id=b.application_id | UNIQUE pair; duplicate rejected |
| Unique interview round | For i,j ∈ I, same application and round ⇒ same interview_id | UNIQUE pair; duplicate rejected |
| Selected resume belongs to applicant | σ_(a.student_id ≠ r.student_id)((A a ⋈_(a.application_id = ar.application_id) AR ar) ⋈_(ar.resume_id = r.resume_id) R r) = ∅ | Two assignment triggers; two immutable-owner triggers; rejected INSERT and UPDATE tests |
| Assignment parents exist | π_application_id(AR) ⊆ π_application_id(A), π_resume_id(AR) ⊆ π_resume_id(R) | NOT NULL FKs; parent deletes restricted |
| Priority in range | σ_(priority < 1 ∨ priority > 5)(A) = ∅ | NOT NULL and CHECK; both boundaries and NULL rejected |
| Offer dates ordered | σ_(response_deadline < offer_date)(O) = ∅ | CHECK; reverse rejected |
| One offer per application | Same application_id in O ⇒ same offer_id | NOT NULL UNIQUE; duplicate rejected |

The tests also check positive resume version numbers and interview rounds, nonnegative wages, boolean values, optional resumes, zero-applications students, NULL emails, and a create/apply/interview/offer workflow with rollback. Trigger parent reads use FOR UPDATE; owner identifiers cannot change, so an assignment cannot be invalidated by an owner update. Deadlocks remain possible under concurrent clients and should be retried by a future application; this sprint does not claim a concurrency benchmark.

## Weak entity and inheritance decisions

Interview rounds are conceptually existence-dependent on Application, with partial key interview_round. A weak-entity representation would identify an Interview by (application_id, interview_round), through its identifying Application relationship. Our implementation retains interview_id as a surrogate and enforces the conceptual identifier with a NOT NULL UNIQUE pair and an FK. The database restricts parent deletion instead of cascading interview history. ApplicationResume is a dependent relationship table identified by application_id, rather than a new independent entity.

We considered JobPosting subtypes RemotePosting and OnSitePosting. They currently add no distinct attributes; location_type is sufficient and avoids duplicated posting columns. ENUM gives disjoint remote/in_person/hybrid categories and total participation through NOT NULL. This is a type discriminator, not an implemented ISA hierarchy. If separate subtype attributes arise, use JobPosting as supertype and subtype tables with posting_id as PK/FK, then decide total/partial and disjoint/overlap constraints explicitly. Subtype tables can be added when distinct facts or restricted relationships justify them.

The design incorporates the supplied written TA feedback. Further requirements may change the documented assumptions.
