# Sprint 2 SQL reports and transaction

The base schema is unchanged: nine tables, 59 columns and the same ownership constraints. Sprint 2 adds two views, a stored procedure and SQL reports. The original seed stays fixed so earlier checks still run. All examples use synthetic records.

## Run the work

For a fresh installation, run the root schema and seed first. If Sprint 1 is already installed and populated, install only the new views and procedure; do not reload its seed.

```sh
mysql -u root -p < schema.sql
mysql -u root -p < supporting-files/seed.sql
mysql -u root -p < supporting-files/sprint2/views.sql
mysql -u root -p < supporting-files/sprint2/transactions.sql
mysql -u root -p < supporting-files/sprint2/reports.sql
mysql -u root -p < supporting-files/sprint2/equivalence.sql
mysql -u root -p < supporting-files/sprint2/optional_reports.sql
```

The established database name remains `coop_application_tracker_sprint1`; it holds both sprints' work. This avoids renaming or resetting an existing installation. The view installer replaces only the two named views; the routine installer replaces only `ScheduleInterview`. It requires CREATE VIEW (plus DROP for a replacement), CREATE ROUTINE, ALTER ROUTINE and EXECUTE privileges in addition to access to the base tables. DDL commits implicitly. Install outside an active transaction, with a backup for an existing installation.

## Eight advanced reports

| Report | Question and SQL method | Expected result on the fixed seed |
| --- | --- | --- |
| R1 | How many applications, active applications, interviewed applications and offered applications does each student have? Two views, outer joins and conditional aggregation | Students 1/2/3 each have 2 applications; student 4 has 0. Active counts are 2/1/2/0. Interviewed counts are 1/0/0/0; offered counts are 1/0/1/0 |
| R2 | Which employers have at least two tracked applications in Spring 2027? INNER JOIN, WHERE before grouping, HAVING after grouping | Employer 1 has 2; employer 2 has 3 |
| R3 | Which applications have a numerically higher priority than their student's average? Correlated AVG subquery | Application IDs 2, 4 and 5. Higher numbers mean less urgent work |
| R4 | Which students have no interviews? NOT EXISTS over the application/interview join | Student IDs 2, 3 and 4, including the student with no applications |
| R5 | Which applications have no selected resume? LEFT JOIN anti-join | Application IDs 5 and 6 |
| R6 | Which students have a missing resume selection or no applications? UNION and NOT EXISTS | Student IDs 2, 3 and 4, once each |
| R7 | How many applications use each status, including unused statuses? LEFT JOIN and COUNT(child ID) | saved 2; applied/interview/offer/rejected 1 each; withdrawn 0 |
| R8 | Who actually applied to every open posting? Nested NOT EXISTS, a relational-division pattern | Student 1. A saved application with NULL date_applied does not count. If no postings are open, all students qualify |

Header-labelled TSV outputs are saved in `evidence/sprint2/`. They are results from the fixed seed before the verifier's transaction tests change its disposable database. This is correctness evidence on a small fixture, not a performance claim.

## Two reusable views

`ApplicationOverview` has one row per application: student/posting/employer identities and names, current status, priority, optional resume selection, interview count and optional offer ID. Interview rows are grouped before joining. Otherwise two interviews could duplicate the application and offer.

`StudentWorkload` has one row per student, including zero-child cases. It counts applications, active applications, applications with interviews and applications with offers. An application with three rounds counts as one interviewed application. Offers are counted by ID, not wage, because an offer may have zero or NULL wage. Both views use explicit columns and `SQL SECURITY INVOKER`; they do not grant table access. The verifier checks the application view against a different direct query and checks student workload against independently expected rows and scalar-subquery counts.

## Four query-equivalence pairs

| Pair | Equivalent forms | Edge case tested |
| --- | --- | --- |
| E1 | NOT EXISTS vs LEFT JOIN / IS NULL for missing resume selections | No assignments at all |
| E2 | Correlated COUNT vs preaggregated LEFT JOIN / COALESCE for workload | Different students sharing a name; no applications |
| E3 | EXISTS vs JOIN DISTINCT for interviewed applications | Several rounds on one application; no interviews |
| E4 | UNION of two filters vs a single OR filter | NULL source and overlapping branches; UNION ALL would duplicate a matching application |

Each formulation is compared with hand-derived expected rows, preserving duplicates and the requested order. Separate counterexamples show why COUNT(*) on an unmatched outer join, omission of DISTINCT on a many-child join, UNION ALL on overlapping filters and NOT IN with a NULL right side cannot be substituted blindly. The verifier executes all four counterexamples directly.

## Transaction: change status and add an interview

`ScheduleInterview(application_id, round, type, scheduled_at)` locks the target application, rejects missing or terminal applications, finds the non-terminal `interview` status by name, updates the application and inserts the round. It commits both writes together. Its exception handler rolls back and uses RESIGNAL to preserve the original error.

Call it on a **fresh standalone connection** with autocommit enabled, outside any caller transaction. This is a transaction-owning procedure: MySQL START TRANSACTION would implicitly commit an already active transaction, even if autocommit is enabled. The autocommit check rejects disabled autocommit but cannot prove the caller has no explicit transaction. It is not a nested-transaction API.

Example for an unmodified fixed seed (this persists an interview and status change):

```sql
CALL ScheduleInterview(3, 1, 'technical', '2026-11-10 14:00:00');
SELECT application_id, status_name, interview_count
FROM ApplicationOverview WHERE application_id = 3;
```

Use the verifier for a repeatable failure demonstration rather than calling the example repeatedly on the same data. Duplicate rounds, nonpositive rounds and NULL schedules are rejected by the original table constraints. Invalid types and terminal applications are rejected by the procedure. These transition rules belong to this operation; arbitrary manual SQL is not claimed to enforce an entire application state machine.

The tests first add a round to application 2, then request that same round again. The UPDATE happens before the duplicate INSERT fails; a new connection sees the old status and unchanged interview count. A successful call for application 3 is also read from a new connection. NULL-schedule and invalid-round failures separately prove rollback after the status UPDATE. Owner-trigger rejection still passes. The routine serializes updates to the same application, but no concurrent-load or deadlock-retry benchmark is claimed.

InnoDB transactions and existing constraints support these demonstrated atomicity/consistency cases. Fresh-connection reads show committed visibility. This does not test crash recovery or every isolation schedule.

## Optional reports completed

O1 uses CTEs to show the current number and percentage of applications in each status, including zero counts. An empty fixture returns zero percentages through NULLIF/COALESCE. Rounded percentages may not sum to exactly 100. This is a current-state funnel summary, not historical conversion: there is no status-history table.

O2 ranks applications within each student using ROW_NUMBER, ordered by priority, posting_id and application_id. The fixed IDs resolve ties deterministically. Tests cover tied priorities and an empty fixture. Students with no applications have no ranked rows; R1 is the report that includes them.

## Design revalidation

No stored relation, key, FK, attribute or multiplicity changed. Therefore the existing complete diagrams and table-by-table FD/BCNF proofs remain applicable. The views are derived results, not extra entity sets. `docs/CONCEPTUAL_DESIGN_REVIEW.md` still applies: completeness adds requested reports; correctness now checks bags/NULLs; minimality avoids stored counts; expressiveness adds named views and an operation; readability uses explicit report names; self-explanation documents empty-set behavior; extensibility keeps the base model; normality preserves the original relations. All original design, theory, database and migration verifiers are rerun alongside Sprint 2.

## Verification command

```sh
python3 scripts/verify_sprint2.py
```

The same MYSQL_BIN, MYSQL_SOCKET and MYSQL_USER settings as the original verifier apply. It creates a randomly named database and retains it. Use `--output-dir PATH` to save the log and ten report TSVs only after all checks pass. Python -O and PYTHONOPTIMIZE are rejected. Python uses only its standard library. Requirements and source documentation are in README.md and SOURCES.md.
