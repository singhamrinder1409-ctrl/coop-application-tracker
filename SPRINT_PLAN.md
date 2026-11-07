# Sprint 2 report and Sprint 3 plan

Group 3: Amrinder Singh, Jaiman Singh and Aashna Sadeque. We worked together on the tracker. This sprint extends the same nine-table database with advanced reports, two views and a transaction. The [previous report and promised goals](docs/archive/SPRINT1_REPORT_AND_PLAN.md) are retained unchanged.

## Promised goals and results

| Previous goal | Previous limitation | Sprint 2 result and evidence | Status |
| --- | --- | --- | --- |
| S2-1: at least eight advanced reports, expected results and tabular output | Seven basic reports; no complete advanced query pack | Eight new reports cover joins, grouping/HAVING, correlated AVG, EXISTS/NOT EXISTS, UNION and relational division. Header-labelled TSVs and exact-row checks include empty groups and NULL cases. [SQL explanation](docs/ADVANCED_SQL.md), `supporting-files/sprint2/reports.sql`, `evidence/sprint2/R1.tsv` through `R8.tsv` | Delivered |
| S2-2: optional CTE/window work | No CTEs or ranked per-student output | CTE current-status summary and deterministic ROW_NUMBER ranking, with ties and empty-data checks. `supporting-files/sprint2/optional_reports.sql`, `evidence/sprint2/O1.tsv`, `O2.tsv` | Optional goal delivered |
| S2-3: two views and a documented multi-step operation | Reports were ad hoc; no reusable views or status/interview operation | ApplicationOverview and StudentWorkload match direct-query/expected results. ScheduleInterview updates status and inserts a round; induced failures roll back both. A new connection reads successful committed changes. `supporting-files/sprint2/views.sql`, `transactions.sql`, `evidence/sprint2/verification.txt` | Delivered |
| S2-4: at least four equivalent-query pairs and integrity regression | No explicit query-equivalence suite | Four pairs have independently expected results and additional NULL, duplicate, overlap and no-child cases. Four counterexamples explain unsafe substitutions. Owner-trigger rejection and all original checks pass. `supporting-files/sprint2/equivalence.sql`, `scripts/verify_sprint2.py`, `evidence/sprint2/regression.txt` | Delivered |
| S2-5: design revalidation and feedback response | New SQL could introduce incorrect counts or contradict the model | Base tables, 59 columns, keys, FKs and multiplicities remain unchanged. All eight quality criteria are revisited in [the SQL report](docs/ADVANCED_SQL.md); the original diagram, FD and theory checks pass. Supplied feedback is addressed below | Delivered using the supplied feedback; no new TA meeting claimed |
| S2-6: clean reproduction, outputs, final hash, video and access | Technical evidence did not establish recording or upload | Run instructions, six verification commands and saved outputs are supplied. The clean-copy result is in `evidence/sprint2/regression.txt`. Recording, measured duration, instructor/TA access and Brightspace submission require team confirmation | Repository/evidence work delivered; human submission steps unverified |

## Response to Sprint 1 feedback

The supplied feedback records 380/400: 90 for delivery evidence, 100 for missed-goal justification, 100 for course-level planning and 90 for module coverage. It contains no written criterion comments. We therefore do not attribute a specific technical criticism to the TA.

For delivery evidence, every promised goal above now points to its SQL, expected output and runnable check. Failure tests require the intended MySQL error and separately read the resulting state; merely printing an error is not treated as proof of rollback. For module coverage, the topic matrix below connects each SQL method to a report or test and makes the next sprint's acceptance criteria explicit. These changes address the two lower-scoring areas without claiming a guaranteed grade.

## What the implementation demonstrates

The [SQL report](docs/ADVANCED_SQL.md) explains each query and its edge cases. R1 preserves students with zero applications. R7 preserves unused statuses. R8 distinguishes saved applications from actual applications and tests the empty-set interpretation of “every open posting.” The views count interviews before joining, so several rounds do not duplicate an offer. Equivalence checks preserve bag multiplicities rather than comparing only distinct sets.

The stored procedure uses a transaction and an error handler. A duplicate-round failure occurs after its status UPDATE; a separate connection then sees the old status. A successful call commits both writes and is read by another connection. These are tested atomicity, consistency and committed-visibility examples, not a claim about every concurrency or crash scenario.

## Missed goals and technical limits

All core implementation goals and the optional CTE/window goal have supporting results. No new entity set or stored attribute was needed, so redrawing the unchanged model would add no information. The original diagrams and design checks remain applicable.

The operation must run on a fresh standalone connection, outside a caller transaction. MySQL START TRANSACTION can implicitly commit an existing transaction; disabled autocommit is rejected, but enabled autocommit alone does not prove that no explicit transaction is open. DDL installation also commits implicitly. The SQL report documents these boundaries.

The fixture is small and synthetic. We have not measured large-data speed, compared physical join algorithms or tested deadlock retries. Those are next-sprint work, not missed promises disguised as completed tests. The current-status summary is not a historical conversion funnel because the tracker stores no status history. A chart and API remain outside the core scope.

No extra Advanced SQL or query-algorithm course material was supplied. The named module boundaries come from the assignment; the detailed topic coverage below and proposed next-sprint experiments are our explicit interpretation. They can be adjusted if the teaching team supplies more specific requirements. We do not rely on the pasted “first attempt is worth 0%” sentence to establish Sprint 2's assessment weight.

## Current scope through Advanced SQL

| Topic | Current evidence | Objective check |
| --- | --- | --- |
| INNER/LEFT JOIN and missing children | R1, R2, R5, R7; both views | Exact rows include zero applications/status counts and optional relationships |
| GROUP BY, WHERE and HAVING | R2 and R7 | Two qualifying employers; unused status remains zero |
| Correlated subqueries | R3 and E2 | Application IDs 2/4/5; counts 2/2/2/0 |
| EXISTS/NOT EXISTS and relational division | R4, R8, E1, E3 | No-interview students, saved-only applications, no open postings and a new unmatched posting |
| Set operations and bag/NULL semantics | R6, E4 and counterexamples | UNION removes overlap; UNION ALL duplicates it; NOT IN with NULL loses valid rows |
| Views and derived aggregation | ApplicationOverview, StudentWorkload | Direct-query equality and independently expected counts; extra interview does not multiply offers |
| Transactions and stored operation | ScheduleInterview | Duplicate, NULL and range failures roll status back; successful writes visible from a new connection |
| CTE and window extensions | O1, O2 | Empty summary avoids division by zero; tied priorities resolve by posting/application IDs |
| Relational design carried forward | Existing diagrams, normalization and constraints | Original design, theory, MySQL and migration suites rerun unchanged |

## Sprint 3: plan through Analysing Query Algorithms

We will share the work across all three members. Core estimate: 18 person-hours plus a 3-hour buffer. These are planning estimates, not measured past velocity. Optional work is reduced first if the core experiments or checks take longer.

| Goal / estimated team effort | Course competency and current limitation | Planned work | Objective end-of-sprint success criteria |
| --- | --- | --- | --- |
| S3-1: controlled datasets / 4h | Data Modelling and Data Analytics: current evidence has only six applications | Generate deterministic synthetic datasets at 1,000, 10,000 and 50,000 applications, including skew, missing children and several interview rounds | Record seed, row/page statistics, database version and fixture assumptions. All FKs, ownership rules and uniqueness checks pass. Hand-worked cases and independently calculated aggregate totals match all affected reports |
| S3-2: page-I/O cost analysis / 4h | Back-end Engineering: no explicit storage/memory cost model | Analyse a selection, projection/duplicate elimination, ordering and a join using relation pages B(R), tuple counts T(R), distinct-value counts and M buffer pages | Give a fully worked numeric example for each operator, state units and assumptions, and compare at least three join algorithms. Show which input-size/memory assumptions change the preferred algorithm; distinguish predicted page I/O from elapsed time |
| S3-3: compare query algorithms / 4h | Back-end Engineering: no physical-plan or access-path evidence | Compare nested-loop, block nested-loop, index nested-loop, sort-merge and hash-join models; inspect at least three real query plans | State model formulas and prerequisites, including hash/sort memory limits and index lookup assumptions. For three report queries, save EXPLAIN and EXPLAIN ANALYZE output at all three scales and map observed operators to the models. Do not assume MySQL exposes or chooses every textbook algorithm |
| S3-4: equivalent queries and indexes / 3h | Data Analytics: equivalent results are checked, but costs are not compared | Compare EXISTS with JOIN DISTINCT and correlated counts with preaggregation; test at least two justified index candidates after inspecting existing PK/FK indexes | Outputs match on all fixtures before any timing claim. Use one warm-up plus five measured runs per variant/scale, record medians and individual timings, and compare plans with/without each candidate. Retain an index only with stated evidence; document scans or regressions rather than promising an improvement |
| S3-5: regression, report and submission / 3h | All three competencies: no reproducible algorithm-analysis package yet | Retain Advanced SQL and design coverage while adding experiment commands, analysis and a measured group video | Every current verifier passes after changes. Fresh-copy experiment commands recreate datasets and results. Report links every planned experiment to actual evidence or a specific missed-goal explanation. Submit final URL/hash/video once and verify recipient access |

### Scope of the algorithm analysis

For a block nested-loop example, state the outer and inner relation and use `B(outer) + ceil(B(outer)/(M-2)) * B(inner)` page I/Os, with M at least 3 and the stated buffer allocation. Compare swapping the outer input. An index nested-loop estimate must include index traversal and matching data-page costs; a two-pass hash estimate assumes partitions fit and no overflow. Sort costs depend on the number of runs and merge passes, not just an in-memory comparison count. These are proposed modelling exercises, not measurements already performed.

The plan also covers selection pushdown, projection/duplicate elimination, sorting, cardinality/selectivity estimates, memory limits and access paths through the four operator analyses and real plans. If a course-specific algorithm is not exposed by MySQL, explain it with a worked page-I/O model and identify the actual operator shown by MySQL instead. Engine estimates, measured rows/times and theoretical costs must be labelled separately.

## Submission

One Group 3 member submits the repository URL, the exact final published commit hash and the video. If private, instructor and TA access must be confirmed. The assignment's formula gives 11 minutes for three members while its numerical example says eight; a video below eight minutes satisfies both. The local recording script targets about 7:30, but only the measured exported file establishes its length. Video scripts and team preparation stay outside the repository.
