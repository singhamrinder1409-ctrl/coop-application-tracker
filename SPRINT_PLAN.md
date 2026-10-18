# Sprint 1 report and Sprint 2 plan

Group 3: Amrinder Singh, Jaiman Singh, Aashna Sadeque. Baseline: kick-off commit `ac978f8` (full hash obtainable with `git rev-parse ac978f8`). The unchanged original commitments are in `docs/archive/KICKOFF_SPRINT_PLAN.md`; the original DDL is archived beside it.

## Delivery: every prior commitment

| Prior goal / success criterion | Previous limitation | Sprint 1 result and independent evidence | Status |
| --- | --- | --- | --- |
| Review schema with TA-client and adjust scope | Kick-off design lacked a complete feedback response | Supplied written TA review incorporated into ERD, normalization and competency planning; corrections and evidence listed in the feedback table below | Delivered using written review; no subsequent approval claimed |
| Improve constraints, especially same-student resume ownership | FK accepted another student's resume; priority allowed NULL | ApplicationResume decomposition, ownership triggers, immutable owners, NOT NULL priority; `schema.sql`, rejected-write checks in `evidence/mysql-verification.txt` | Delivered |
| At least five explicit SQL/algebra constraints | Rules were informally described | Ten formal rules and implementation mapping in `docs/CONSTRAINTS.md` | Delivered |
| Decide whether weak entities/inheritance help | Mentioned but not decided | Interview's partial identifier, surrogate mapping, parent deletion policy, and decision against unnecessary posting subtypes in `docs/CONSTRAINTS.md` | Delivered |
| Better sample data with normal/edge cases | One interview; no empty-workflow case | 4 students, 6 applications, 2 interviews, 2 offers; unused student, optional resumes, multiple versions, NULL email, date/wage boundaries | Delivered; synthetic data explicitly labelled |
| Write more useful reporting queries | Five optional, unverified kick-off queries | Seven verified reports: two new LEFT JOIN reports for zero-application students and missing resume assignments, plus corrected upcoming filter; exact expected rows tested from the report file | Delivered; output in `evidence/demo-output.tsv` |
| Short demo proving workflow | DDL was not execution evidence | Automated create/apply/resume/interview/offer/rollback workflow and rejected writes on MySQL 8.4.8 | Delivered as reproducible demo; team video still to record |

## Delivery: every feedback correction

| TA feedback | Correction | Evidence to show |
| --- | --- | --- |
| BCNF not fully demonstrated table by table | Nine-table FD basis, all keys, closure/minimality/BCNF checks; resume FD resolved by decomposition | `NORMALIZATION.md`, `scripts/design.py`, `evidence/design-verification.txt` |
| ERD omitted most attributes | Complete course-style Chen diagram plus relational companion: all 59 SQL attributes accounted for, including all 13 JobPosting columns | `CONCEPTUAL_ERD.svg`, `CONCEPTUAL_ERD.md`, `ERD.svg`, generated `RELATIONAL_SCHEMA.md` |
| Course competency and current limitation unnamed | Actual lecture competency names (Data Analytics, Data Modelling, Back-end Engineering), concrete limitations and measurable checks | Sprint 2 matrix below |
| Missing FDs in ERDs, minimal bases, projection, 3NF, 4NF | Explicit worked examples, assumptions and proofs/decisions | `NORMALIZATION.md`; not merely future promises |

## Missed goals and technical limits

The implementation evidence covers the prior technical commitments. The supplied written TA review is incorporated; no subsequent meeting or approval is recorded. Resume reuse, one offer per application and immutable owner identifiers remain design assumptions.

The video, repository publication/access and Brightspace upload remain pending. If a later check fails or the TA identifies a missed goal, record the failing behavior, its impact and the revised plan here.

The available course material contains 14 lecture PDFs, one practice-exam PDF, 16 transcripts and three worksheet archives, including Improving Conceptual Designs, ERDs to FDs, Projecting FDs, corrected 3NF, and 4NF/MVDs. Welcome slides 6-8 name the competencies used below: Data Analytics, Data Modelling and Back-end Engineering. `docs/COURSE_ALIGNMENT.md` maps the supplied lectures and new advanced material to concrete project evidence; `docs/CONCEPTUAL_DESIGN_REVIEW.md` applies all eight conceptual-design quality criteria. The SQL workflow provides the current demonstration. The small synthetic fixture supports correctness checks, not a performance conclusion.

## Sprint 2: course-level competencies, current limits and objective measures

The next scope includes material through **Advanced SQL**. Carry forward Advanced Relational Design verification instead of dropping it. Task owners are proposed and need team agreement. Core budget: 18 person-hours total (about 6 per person), with up to 3 additional optional hours and a 3-hour buffer. This is a planning estimate, not a measured team velocity; reduce optional scope first if checks reveal problems.

| Goal / proposed owner / effort | Named course competency area | Current limitation | End-of-sprint success criterion and exact demonstration |
| --- | --- | --- | --- |
| S2-1: reporting query pack / Amrinder / 5h | Data Analytics | Seven basic reports with expected-row tests; no comprehensive nested/analytical SQL pack | Add at least 8 named reports with hand-derived expected rows on a fixed fixture; demonstrate INNER/LEFT JOIN, WHERE versus HAVING, GROUP BY, EXISTS/NOT EXISTS, nested/correlated subqueries, and UNION. Include students with zero applications and NULL values; every expected-result assertion passes. Provide clearly labelled tabular/CSV report output suitable for visualization. A chart or scaled timing experiment is optional; the introductory transcript explicitly excludes visualization quality from course scope |
| S2-2: optional CTE/window analysis / Jaiman / up to 3h | Data Analytics | No CTEs or window functions implemented | CTE-based application funnel and ROW_NUMBER ranking per student; deterministic tie-break by posting_id/application_id; compare both with hand-worked results, including ties and empty groups. Treat this entire goal as optional after core SQL/design acceptance criteria pass; confirm any additional module topics if new material becomes available |
| S2-3: reusable views and safe updates / Aashna / 3h | Back-end Engineering | Reports are ad hoc SQL; transaction rollback is demonstrated, but no reusable views or documented multi-step SQL operation exist | Create two documented views with explicit columns; verify view/direct-query equivalence. Demonstrate a SQL operation that updates status and adds an interview in one transaction, with an induced failure proving neither write persists. Verify committed writes from a new connection and document what the tests demonstrate about atomicity/consistency. An API, restricted-account integration, and a full concurrency benchmark are optional later work, not core next-sprint promises |
| S2-4: semantics and integrity regression / Jaiman with team / 4h | Back-end Engineering and Data Modelling | Existing tests verify fixed fixtures, but no SQL-equivalence or concurrent-client cases | At least 4 equivalent-query pairs match on NULL, duplicates, no-child, and multiple-child cases; distinguish COUNT(*) from COUNT(child_id); rerun all Sprint 1 checks after schema changes. Document trigger/transaction behavior, including one rejected ownership attempt |
| S2-5: design revalidation and client feedback / all / 3h | Data Modelling | Written feedback incorporated; changed requirements could introduce new dependencies | Record and respond to any new TA feedback if supplied; map the assignment scope and feedback topics through Advanced SQL to a file, test or justified design decision; regenerate diagram and FD report after any model change; explain any new dependency with a losslessness/preservation check. Apply all eight conceptual quality criteria and rerun full 3NF synthesis/key-relation and formal MVD example checks |
| S2-6: evidence and submission / all / 3h | All three competencies: reproducible evidence | No recorded Sprint 1 video or published repository URL yet | Reproduce from clean clone; save actual outputs, exact commit hash, and measured video length; ensure TA access and one group submission |

## Module-level coverage matrix

This list maps the assignment, feedback and all 34 supplied material files. Exact lecture titles, slide references and objective mappings are in `docs/COURSE_ALIGNMENT.md`. Advanced Relational Design is now directly supported by the added PDFs and worksheets. A separate Advanced SQL deck is still absent; the core plan therefore covers the named SQL operations and labels CTE/window work as optional.

| Module/topic | Sprint 1 baseline | Sprint 2 evidence / objective check |
| --- | --- | --- |
| SQL storage and DDL | Nine executable tables, keys, checks, triggers | Clean schema load and full rejected-write regression pass |
| SQL querying / relational operations | Seven reports with exact-row assertions | S2-1 expected rows, joins, aggregation, HAVING, subqueries, set operations |
| Conceptual design and multiplicity | Chen conceptual model, complete relational attributes and relationship cardinalities | S2-5 regenerate ERD; reconcile every DDL attribute and FK |
| FDs, keys and BCNF | Exhaustive closures under declared model; table-by-table checks | S2-5 rerun all keys and BCNF checks after changes |
| Relational algebra constraints | Ten explicit rules | S2-4 map each rule to SQL enforcement and counterexample |
| Inheritance and weak entity sets | Explicit design decisions | S2-5 revisit only if requirements add subtype-specific facts |
| Conceptual quality criteria | Eight-criterion project review and transformation classification | S2-5 re-evaluate completeness, correctness, minimality, expressiveness, readability, self-explanation, extensibility and normality |
| Advanced Relational Design: FDs in ERDs | Identifier and multiplicity implications explained | S2-5 check new relationships against FD model |
| Advanced Relational Design: minimal bases and projection | Worked reduction and inferred projected FD | S2-5 compute closure/projection for any changed relation |
| Advanced Relational Design: 3NF | Prime attributes, preservation tradeoff and complete synthesis including added key relation | S2-5 compare 3NF/BCNF if new FDs require a tradeoff |
| Advanced Relational Design: 4NF | Formal tuple-swap definition, triviality/complementarity, non-splitting counterexample and lossless decomposition | S2-5 split independent multivalued requirements if added; demonstrate lossless join |
| Advanced SQL: NULL, bag/set semantics, outer joins | Edge fixture exists; limited assertions | S2-1/S2-4 explicit expected rows and equivalence cases |
| Advanced SQL: views, nested queries, EXISTS, set operations | Not yet implemented as a comprehensive pack | S2-1/S2-3 named query/view outputs and assertions |
| Proposed extension: CTEs/window functions | Not implemented | S2-2 expected rankings/funnel; explicitly planned extensions |

The introductory transcript distinguishes competency stages: syntactically/semantically correct SQL before advanced aggregation and subqueries; normalized models before justified design improvements; and transaction/ACID foundations before an aspirational API. This plan prioritizes those core steps. Visualizations, APIs and physical-plan optimization are not added as mandatory Sprint 1 deliverables.

## Extension of the kick-off implementation

The Desktop kick-off copy matches every tracked baseline file byte for byte, despite having a separate Git history. Work continues in this research checkout. `migrations/001_sprint1.sql` upgrades the exact original eight-table schema and preserves all four original application/resume assignments; 15 migration checks demonstrate preservation and preflight rejection of invalid ownership. Verification ran on separate test databases; the Desktop project was unchanged. See `migrations/README.md` for the upgrade procedure and MySQL DDL transaction limits.

## Recording strategy

Use `TEAM_VIDEO_SCRIPT.md`, target 7:30 including transitions, and show live commands and their results. The formula 5 + 2 × 3 gives 11 minutes, while the pasted assignment's numerical example says 8; a video below 8 minutes satisfies both interpretations. Measure the exported file rather than estimating by script length. Every goal must be mentioned, including the written TA review and resulting corrections; show the plan's current-limit column, not only task names.
