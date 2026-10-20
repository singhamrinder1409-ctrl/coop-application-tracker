# Co-op Application Tracker - CSC 370 Sprint 1

Group 3: Amrinder Singh (`amrinder`), Jaiman Singh (`jaiman1`), Aashna Sadeque (`aashnas`). We worked together on the design, implementation, verification and documentation.

This MySQL database tracks students' co-op applications, job postings, resume selections, interview rounds and offers. Sprint 1 extends the kick-off implementation with a normalized resume-selection relationship, stronger integrity rules, complete diagrams and reproducible verification. All demonstration data is synthetic.

## Guide to the submission

Start with the [Sprint 1 report and Sprint 2 plan](SPRINT_PLAN.md). It compares the prior commitments with delivered results, addresses the kick-off feedback and sets measurable goals through Advanced SQL.

| Grading criterion | Evidence |
| --- | --- |
| Achievement of sprint goals | The report's prior-commitment and feedback tables link each result to its implementation or verification. [Saved results](evidence/README.md) include seven report outputs, valid workflows, rejected writes and migration checks. |
| Justification for missed goals | The report's technical-limits section distinguishes completed work, design assumptions and unverified submission actions. No subsequent TA meeting or approval is claimed. |
| Improvement in course-level competencies | The next-sprint matrix names Data Analytics, Data Modelling and Back-end Engineering, with current limitations, shared team responsibility, effort and objective success criteria. |
| Coverage of new module competencies | The [course mapping](docs/COURSE_ALIGNMENT.md) connects current work through Advanced Relational Design and planned work through Advanced SQL to evidence and checks. |

## Design and feedback corrections

| Topic | Files |
| --- | --- |
| Complete conceptual model and participation | [Chen ERD and explanation](CONCEPTUAL_ERD.md) |
| All nine tables and 59 columns | [Relational ERD](ERD.md), [schema reference](RELATIONAL_SCHEMA.md), [executable DDL](schema.sql) |
| Table-by-table BCNF, FDs, keys, minimal bases, projection, 3NF and 4NF | [Normalization report](NORMALIZATION.md) |
| SQL and relational-algebra constraints; weak entities and inheritance | [Integrity rules and design decisions](docs/CONSTRAINTS.md) |
| Eight conceptual-design quality criteria | [Design review](docs/CONCEPTUAL_DESIGN_REVIEW.md) |
| Preservation of the kick-off data | [Saved migration results](evidence/migration-verification.txt) |
| References and assistance acknowledgement | [Sources](SOURCES.md) |

The original kickoff plan, DDL and seed are retained in `docs/archive/` as the comparison baseline. They describe the earlier version; the files linked above describe Sprint 1.

## Run the database and reports

Requirement: MySQL 8.0.16 or later. Recorded database verification used MySQL 8.4.8. All nine tables explicitly use InnoDB.

Run these commands from the repository root with a MySQL account permitted to create databases, tables and triggers and execute SELECT, INSERT, UPDATE and DELETE:

```sh
mysql -u root -p < schema.sql
mysql -u root -p < supporting-files/seed.sql
mysql -u root -p < supporting-files/demo_queries.sql
```

This creates `coop_application_tracker_sprint1`. Existing tables cause the load to stop; the current schema does not drop a database. Use a fresh installation for these commands rather than loading the seed over existing data. The archived kickoff DDL is historical and includes a database reset; it is not the current setup command.

## Verification evidence

The [evidence index](evidence/README.md) describes the saved results: 56 database checks, 15 migration checks, 12 worked theory checks, 10 design checks and two conceptual-diagram coverage checks. The [seven report outputs](evidence/demo-output.tsv) can be compared with a fresh run of the supplied schema, seed and report SQL.

These are recorded verification results from the development version. The Python verification/generation tools and optional migration implementation are retained locally, outside this submission checkout. Their recorded results remain here as supporting evidence; the automated suites cannot be rerun from this checkout alone. The SQL demonstration and written design proofs can be checked using the files included here. Domain assumptions and 4NF reasoning are documented in the normalization report.
