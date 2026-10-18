# Sprint 1 report and Sprint 2 plan

Group 3: Amrinder Singh, Jaiman Singh, Aashna Sadeque. Baseline: kick-off commit `ac978f8` (full hash obtainable with `git rev-parse ac978f8`). The unchanged original commitments are in `docs/archive/KICKOFF_SPRINT_PLAN.md`; the original DDL is archived beside it.

## Delivery: every prior commitment

| Prior goal / success criterion | Previous limitation | Sprint 1 result and independent evidence | Status |
| --- | --- | --- | --- |
| Review schema with TA-client and adjust scope | Kick-off design lacked a complete feedback response | Supplied written TA review incorporated into ERD, normalization and competency planning; traceable response in `RUBRIC_AUDIT.md` | Delivered using written review; no subsequent approval claimed |
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

No implementation goal from the prior plan is currently known to be missed. The TA-review commitment is evidenced by the supplied written review and the changes made in response; neither the assignment nor the prior plan requires a live meeting. We do not claim a new meeting or approval of this revision. Resume reuse, one offer per application, and immutable owner identifiers are documented design assumptions, not newly supplied TA requirements.

The delivery packet is not yet submitted: the actual video, remote repository publication/access and Brightspace upload remain. These are submission tasks rather than fabricated technical setbacks. If a later run or TA review reveals a missed goal, record the concrete failing behavior, evidence and impact here rather than inventing an explanation.

The group confirmed no separate competency list or additional TA requirements. The subsequently supplied Desktop course folder contains lectures 01-09. The Welcome lecture, slides 6-8, provides the actual competency names used below: Data Analytics, Data Modelling and Back-end Engineering. `docs/COURSE_ALIGNMENT.md` maps all nine supplied lectures and distinguishes feedback-required advanced topics from the available slide inventory. No UI was promised by the original plan; the SQL workflow is this sprint's demonstrable system. We make no performance claim from a tiny fixture and no claim to have recorded/uploaded a video or shared repository.

## Sprint 2: course-level competencies, current limits and objective measures

The next scope includes material through **Advanced SQL**. Carry forward Advanced Relational Design verification instead of dropping it. These are proposed owners to confirm within the team, not statements about who performed this session's work. Budget 21 person-hours total (about 7 per person), plus a 3-hour buffer. This is a planning estimate, not a measured team velocity; reduce optional scope first if checks reveal problems.

| Goal / proposed owner / effort | Named course competency area | Current limitation | End-of-sprint success criterion and exact demonstration |
| --- | --- | --- | --- |
| S2-1: reporting query pack / Amrinder / 5h | Data Analytics | Seven basic reports with expected-row tests; no complex query pack, chart or scaled timing evidence | Add at least 8 named reports with hand-derived expected rows on a fixed fixture; demonstrate INNER/LEFT JOIN, WHERE versus HAVING, GROUP BY, EXISTS/NOT EXISTS, nested/correlated subqueries, and UNION. Include students with zero applications and NULL values; every expected-result assertion passes. Add one chart whose values match a report. On a deterministic 1,000-application fixture, record EXPLAIN, hardware and three warm timings per report; target median below 1 second and explain any miss |
| S2-2: CTE/window analysis / Jaiman / 2h | Data Analytics | No CTEs or window functions implemented | CTE-based application funnel and ROW_NUMBER ranking per student; deterministic tie-break by posting_id/application_id; compare both with hand-worked results, including ties and empty groups. Treat CTEs and window functions as planned extensions within the Advanced SQL work |
| S2-3: reusable views and safe updates / Aashna / 5h | Back-end Engineering | Reports are ad hoc SQL; no reusable views, API/client operation or role-restricted access tests exist | Create two documented views with explicit columns; verify view/direct-query equivalence; parameterized client operation updates status and adds an interview in one transaction, with an induced failure proving neither write persists. Use a restricted DB account: expected reads/status updates/interview inserts succeed and a forbidden schema change is denied |
| S2-4: semantics and integrity regression / all / 4h | Back-end Engineering and Data Modelling | Existing tests verify fixed fixtures, but no SQL-equivalence or concurrent-client cases | At least 4 equivalent-query pairs match on NULL, duplicates, no-child, and multiple-child cases; distinguish COUNT(*) from COUNT(child_id); rerun all Sprint 1 checks after schema changes. Document trigger/transaction behavior, including one rejected ownership attempt |
| S2-5: design revalidation and client feedback / all / 2h | Data Modelling | Written feedback incorporated; changed requirements could introduce new dependencies | Record and respond to any new TA feedback if supplied; map the assignment scope and feedback topics through Advanced SQL to a file, test or justified design decision; regenerate diagram and FD report after any model change; explain any new dependency with a losslessness/preservation check |
| S2-6: evidence and submission / all / 3h | All three competencies: reproducible evidence | No recorded Sprint 1 video or published repository URL yet | Reproduce from clean clone; save actual outputs, exact commit hash, and measured video length; ensure TA access and one group submission |

## Module-level coverage matrix

This list maps the assignment, feedback and all nine supplied lectures. Exact lecture titles, slide references and objective mappings are in `docs/COURSE_ALIGNMENT.md`. Separate Advanced Relational Design and Advanced SQL decks were not present; include the feedback topics and state proposed Advanced SQL extensions explicitly.

| Module/topic | Sprint 1 baseline | Sprint 2 evidence / objective check |
| --- | --- | --- |
| SQL storage and DDL | Nine executable tables, keys, checks, triggers | Clean schema load and full rejected-write regression pass |
| SQL querying / relational operations | Seven reports with exact-row assertions | S2-1 expected rows, joins, aggregation, HAVING, subqueries, set operations |
| Conceptual design and multiplicity | Chen conceptual model, complete relational attributes and relationship cardinalities | S2-5 regenerate ERD; reconcile every DDL attribute and FK |
| FDs, keys and BCNF | Exhaustive closures under declared model; table-by-table checks | S2-5 rerun all keys and BCNF checks after changes |
| Relational algebra constraints | Ten explicit rules | S2-4 map each rule to SQL enforcement and counterexample |
| Inheritance and weak entity sets | Explicit design decisions | S2-5 revisit only if requirements add subtype-specific facts |
| Advanced Relational Design: FDs in ERDs | Identifier and multiplicity implications explained | S2-5 check new relationships against FD model |
| Advanced Relational Design: minimal bases and projection | Worked reduction and inferred projected FD | S2-5 compute closure/projection for any changed relation |
| Advanced Relational Design: 3NF | Prime-attribute example; dependency preservation tradeoff | S2-5 compare 3NF/BCNF if new FDs require a tradeoff |
| Advanced Relational Design: 4NF | Independent skill/city MVD example; domain assumption review | S2-5 split independent multivalued requirements if added; demonstrate lossless join |
| Advanced SQL: NULL, bag/set semantics, outer joins | Edge fixture exists; limited assertions | S2-1/S2-4 explicit expected rows and equivalence cases |
| Advanced SQL: views, nested queries, EXISTS, set operations | Not yet implemented as a comprehensive pack | S2-1/S2-3 named query/view outputs and assertions |
| Proposed extension: CTEs/window functions | Not implemented | S2-2 expected rankings/funnel; explicitly planned extensions |

## Extension of the kick-off implementation

The Desktop kick-off copy matches every tracked baseline file byte for byte, despite having a separate Git history. Work continues in this research checkout. `migrations/001_sprint1.sql` upgrades the exact original eight-table schema and preserves all four original application/resume assignments; 13 migration checks demonstrate preservation and preflight rejection of invalid ownership. The Desktop project and the user’s existing MySQL data were not overwritten. See `migrations/README.md` for the upgrade procedure and MySQL DDL transaction limits.

## Recording strategy

Use `TEAM_VIDEO_SCRIPT.md`, target 7:30 including transitions, and show live commands and their results. The formula 5 + 2 × 3 gives 11 minutes, while the pasted assignment's numerical example says 8; a video below 8 minutes satisfies both interpretations. Measure the exported file rather than estimating by script length. Every goal must be mentioned, including the written TA review and resulting corrections; show the plan's current-limit column, not only task names.
