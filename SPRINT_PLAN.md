# Sprint 1 report and Sprint 2 plan

Group 3: Amrinder Singh, Jaiman Singh, Aashna Sadeque. Baseline: kick-off commit `ac978f8` (full hash obtainable with `git rev-parse ac978f8`). The unchanged original commitments are in `docs/archive/KICKOFF_SPRINT_PLAN.md`; the original DDL is archived beside it.

## Delivery: every prior commitment

| Prior goal / success criterion | Previous limitation | Sprint 1 result and independent evidence | Status |
| --- | --- | --- | --- |
| Review schema with TA-client and adjust scope | No recorded TA requirements | Attached written feedback used to repair ERD, normalization and plans; no live consultation claimed | Partial: live review still pending |
| Improve constraints, especially same-student resume ownership | FK accepted another student's resume; priority allowed NULL | ApplicationResume decomposition, ownership triggers, immutable owners, NOT NULL priority; `schema.sql`, rejected-write checks in `evidence/mysql-verification.txt` | Delivered |
| At least five explicit SQL/algebra constraints | Rules were informally described | Ten formal rules and implementation mapping in `docs/CONSTRAINTS.md` | Delivered |
| Decide whether weak entities/inheritance help | Mentioned but not decided | Interview's partial identifier, surrogate mapping, parent deletion policy, and decision against unnecessary posting subtypes in `docs/CONSTRAINTS.md` | Delivered |
| Better sample data with normal/edge cases | One interview; no empty-workflow case | 4 students, 6 applications, 2 interviews, 2 offers; unused student, optional resumes, multiple versions, NULL email, date/wage boundaries | Delivered; synthetic data explicitly labelled |
| Useful reporting queries | Optional unverified queries | Five executable reports, deterministic as-of filter for upcoming interviews; output in `evidence/demo-output.tsv` | Delivered |
| Short demo proving workflow | DDL was not execution evidence | Automated create/apply/resume/interview/offer/rollback workflow and rejected writes on MySQL 8.4.8 | Delivered as reproducible demo; team video still to record |

## Delivery: every feedback correction

| TA feedback | Correction | Evidence to show |
| --- | --- | --- |
| BCNF not fully demonstrated table by table | Nine-table FD basis, all keys, closure/minimality/BCNF checks; resume FD resolved by decomposition | `NORMALIZATION.md`, `scripts/design.py`, `evidence/design-verification.txt` |
| ERD omitted most attributes | All SQL attributes now shown, including all 13 JobPosting columns | `ERD.svg`, `ERD.md`, generated `RELATIONAL_SCHEMA.md` |
| Course competency and current limitation unnamed | Named competency areas, concrete current limitations, measurable checks | Sprint 2 matrix below |
| Missing FDs in ERDs, minimal bases, projection, 3NF, 4NF | Explicit worked examples, assumptions and proofs/decisions | `NORMALIZATION.md`; not merely future promises |

## Missed goals and technical limits

A live TA-client review has not occurred in this work session. Written feedback is addressed, but it cannot verify new stakeholder assumptions. The remaining action is to confirm resume reuse, one offer per application, and immutable owner policy with the TA; record the response before expanding the schema. This is a pending validation task, not a fabricated technical blocker or a completed interview.

The group confirmed that there is no separate competency list or additional TA-client requirement. The assignment and written feedback are the available requirements. The named competencies below are project mappings to that scope, rather than quotations from a separate syllabus. No UI was promised by the original plan; the SQL workflow is this sprint's demonstrable system. We make no performance claim from a tiny fixture and no claim to have recorded/uploaded a video or shared repository.

## Sprint 2: course-level competencies, current limits and objective measures

The next scope includes material through **Advanced SQL**. Carry forward Advanced Relational Design verification instead of dropping it. These are proposed owners to confirm within the team, not statements about who performed this session's work. Budget 18 person-hours total (6 per person), plus a 3-hour buffer; reduce optional scope first if checks reveal problems.

| Goal / proposed owner / effort | Named course competency area | Current limitation | End-of-sprint success criterion and exact demonstration |
| --- | --- | --- | --- |
| S2-1: reporting query pack / Amrinder / 4h | Express information needs using SQL and relational operations | Current pack has five simple joins/filters; no tested complex reporting | Add at least 8 named reports with hand-derived expected rows on a fixed fixture; demonstrate INNER/LEFT JOIN, WHERE versus HAVING, GROUP BY, EXISTS/NOT EXISTS, nested/correlated subqueries, and UNION. Include students with zero applications and NULL values; every expected-result assertion passes |
| S2-2: CTE/window analysis / Jaiman / 3h | Formulate and explain advanced SQL queries | No CTEs or window functions implemented | CTE-based application funnel and ROW_NUMBER ranking per student; deterministic tie-break by posting_id/application_id; compare both with hand-worked results, including ties and empty groups. Treat CTEs and window functions as planned extensions within the Advanced SQL work |
| S2-3: reusable views and safe updates / Aashna / 3h | Build a reliable database-backed information system | Reports are ad hoc SQL and no reusable views exist | Create two documented views with explicit columns; verify view/direct-query equivalence; parameterized client operation updates status and adds an interview in one transaction, with an induced failure proving neither write persists |
| S2-4: semantics and integrity regression / all / 3h | Reason about correctness, constraints and query semantics | Existing tests verify fixed fixtures, but no SQL-equivalence or concurrent-client cases | At least 4 equivalent-query pairs match on NULL, duplicates, no-child, and multiple-child cases; distinguish COUNT(*) from COUNT(child_id); rerun all Sprint 1 checks after schema changes. Document trigger/transaction behavior, including one rejected ownership attempt |
| S2-5: design revalidation and client feedback / all / 2h | Model requirements and evaluate relational designs | Domain assumptions not confirmed by live TA; written feedback is the available client input | Record TA response or explicitly report contact pending; map the assignment scope and feedback topics through Advanced SQL to a file, test or justified design decision; regenerate diagram and FD report after any model change; explain any new dependency with a losslessness/preservation check |
| S2-6: evidence and submission / all / 3h | Communicate technical progress with reproducible evidence | No recorded Sprint 1 video or published repository URL yet | Reproduce from clean clone; save actual outputs, exact commit hash, and measured video length; ensure TA access and one group submission |

## Module-level coverage matrix

This list covers the known topics in the feedback and a proposed Advanced SQL scope. The group confirmed that no separate list is available. This matrix maps the supplied scope and feedback; it does not quote an official syllabus.

| Module/topic | Sprint 1 baseline | Sprint 2 evidence / objective check |
| --- | --- | --- |
| SQL storage and DDL | Nine executable tables, keys, checks, triggers | Clean schema load and full rejected-write regression pass |
| SQL querying / relational operations | Five reports | S2-1 expected rows, joins, aggregation, HAVING, subqueries, set operations |
| Conceptual design and multiplicity | Complete entity attributes and relationship cardinalities | S2-5 regenerate ERD; reconcile every DDL attribute and FK |
| FDs, keys and BCNF | Exhaustive closures under declared model; table-by-table checks | S2-5 rerun all keys and BCNF checks after changes |
| Relational algebra constraints | Ten explicit rules | S2-4 map each rule to SQL enforcement and counterexample |
| Inheritance and weak entity sets | Explicit design decisions | S2-5 revisit only if requirements add subtype-specific facts |
| Advanced Relational Design: FDs in ERDs | Identifier and multiplicity implications explained | S2-5 check new relationships against FD model |
| Advanced Relational Design: minimal bases and projection | Worked reduction and inferred projected FD | S2-5 compute closure/projection for any changed relation |
| Advanced Relational Design: 3NF | Prime-attribute example; dependency preservation tradeoff | S2-5 compare 3NF/BCNF if new FDs require a tradeoff |
| Advanced Relational Design: 4NF | Independent skill/city MVD example; domain assumption review | S2-5 split independent multivalued requirements if added; demonstrate lossless join |
| Advanced SQL: NULL, bag/set semantics, outer joins | Edge fixture exists; limited assertions | S2-1/S2-4 explicit expected rows and equivalence cases |
| Advanced SQL: views, nested queries, EXISTS, set operations | Not yet implemented as a comprehensive pack | S2-1/S2-3 named query/view outputs and assertions |
| Proposed extension: CTEs/window functions | Not implemented | S2-2 expected rankings/funnel; verify module scope with TA |

## Recording strategy

Use `TEAM_VIDEO_SCRIPT.md`, target 7:30 including transitions, and show live commands and their results. The formula 5 + 2 × 3 gives 11 minutes, while the pasted assignment's numerical example says 8; a video below 8 minutes satisfies both interpretations. Measure the exported file rather than estimating by script length. Every goal must be mentioned, including the pending TA review; show the plan's current-limit column, not only task names.
