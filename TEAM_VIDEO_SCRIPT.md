# Sprint 1 team recording script - target 7:30

Proposed speaking split: Amrinder 0:00-2:30, Jaiman 2:30-5:00, Aashna 5:00-7:30. Rehearse and adapt this to your actual contribution and understanding. The video is not recorded by this script. Keep final export below 8 minutes, including titles/transitions, to satisfy both the formula and inconsistent example in the supplied assignment text.

Prepare: open the project folder, ERD.svg, NORMALIZATION.md, docs/CONSTRAINTS.md and SPRINT_PLAN.md. Have MySQL running and verify credentials before recording. Run `python3 scripts/design.py` and `python3 scripts/verify.py` live if possible. The saved evidence is available for inspection but should not be described as your own live run unless you actually run it. Show the exact submission commit via `git rev-parse HEAD`.

## 0:00-2:30 - Amrinder: goals, feedback, complete model

**0:00-0:35 — show SPRINT_PLAN.md, delivery table.**

“We are Group 3, Amrinder, Jaiman and Aashna. Our Co-op Application Tracker connects students, employers, postings, applications, resume versions, interviews and offers. We are reporting against our kick-off plan, preserved in the archive. We promised a schema review, stronger constraints, relational algebra rules, advanced modelling decisions, edge-case data, reports and a working workflow demo.”

**0:35-1:00 — show feedback correction table.**

“The feedback asked us to show every ERD attribute, prove BCNF per table, state current limitations against course competencies, and cover minimal bases, projecting FDs, 3NF and 4NF. Those now have explicit evidence. We used the written feedback, but a live TA review remains pending; we have not claimed it happened.”

**1:00-1:45 — zoom ERD.svg.**

“Every SQL attribute appears in the new diagram, including all 13 JobPosting columns. One employer has zero or many postings, each posting has exactly one employer. Each application has one student, posting and status, zero or many interviews and at most one offer. Selected resumes are represented by ApplicationResume. A missing row means no resume has been selected. A resume can be reused across applications belonging to its owner.”

**1:45-2:30 — show schema.sql and docs/CONSTRAINTS.md.**

“Resume ownership was previously unenforced. We now check it when an assignment is inserted or changed, and prevent changing a record's owner. The rules include foreign keys, uniqueness, date ordering and bounded priority. Interview has a conceptual partial key, the round number within its application; our surrogate key is supplemented by that unique pair. Separate posting subtype tables would currently add no distinct facts, so we keep a required location type and explain when inheritance would become useful.”

## 2:30-5:00 - Jaiman: normalization and Advanced Relational Design

**2:30-3:20 — show NORMALIZATION.md, nine-table table.**

“Our BCNF claim is now relative to stated domain FDs. Each table has a singleton-right-side minimal basis and all candidate keys listed. For example, a student and version number identify a resume, and an application and round identify an interview. Closures prove these keys. Nullable unique emails and URLs are not treated as unconditional classical keys. The checker computes closures for all attribute subsets and checks that every nontrivial determinant is a superkey.”

**3:20-3:55 — show resume decomposition.**

“Adding a same-owner constraint to the old table would leave resume determining student within Application. A resume can be reused, so resume is not an application key. We removed resume selection from Application. The selected-resume relation stores application and resume, while ResumeVersion stores its owner. Joining on resume is lossless for the assigned-resume fragment because resume determines the owner. A cross-table trigger still ensures the applicant equals that owner.”

**3:55-4:25 — show minimal basis / projection example.**

“In the example, application determines student and posting; student determines name. Application determining name is redundant by transitivity. Projecting onto application, name and posting must nevertheless retain application determining name. Projection means deriving implied FDs using closures, not just deleting FDs that mention removed attributes.”

**4:25-5:00 — show 3NF and 4NF examples, run design.py.**

“3NF allows a non-key determinant if the right-side attribute is prime; BCNF does not. The allocation example shows why a lossless BCNF decomposition can lose local dependency enforcement. For 4NF, independently varying skills and cities create a cross-product and should be separate relations. We state the production model's single-valued assumptions; the FD checker alone does not prove 4NF. Here are the actual key, minimality and BCNF checks passing.”

## 5:00-7:30 - Aashna: execution evidence, limits and next sprint

**5:00-5:55 — run verify.py; show output.**

“The database checks load the DDL and seed into a fresh test schema on MySQL. They test a valid application, resume selection, interview and offer in a transaction and then prove rollback restored the fixture. They also try invalid writes: another student's resume, duplicate applications and rounds, invalid priority, negative wages and reversed deadlines. Each expected rejection is checked against a MySQL error code, rather than treating any error as success.”

**5:55-6:20 — show demo-output.tsv and fixture.**

“We have four students and six applications, including one student with no applications and applications without selected resumes. The five reports show applications, active applications, upcoming interviews, status counts and offers. The upcoming-interview query uses a fixed demonstration date and excludes the earlier interview. Sample employers and jobs are synthetic.”

**6:20-7:15 — show Sprint 2 matrix, emphasizing current limitations.**

“For next sprint, the course competency areas are modelling, SQL querying, correctness and database-backed system development. Our current limitation is that reports use basic joins and filters, without a tested advanced query pack or reusable views. We plan eight reports covering outer joins, grouping, HAVING, correlated queries, EXISTS and set operations, with expected rows. We also plan two views and a transactional update with failure rollback. CTEs and window rankings are proposed pending confirmation of the exact module scope. The plan includes named owners, effort, edge cases and measurable tests. It retains FD and integrity regression through Advanced Relational Design. The official Brightspace competency wording was not supplied, so the group must reconcile this matrix before submitting.”

**7:15-7:30 — show checklist and git rev-parse HEAD.**

“The remaining tasks are the TA review, official competency check, recording, and repository publication/access. Our submission must identify the exact commit shown here. We will submit one repository link, commit hash and measured video for Group 3.”
