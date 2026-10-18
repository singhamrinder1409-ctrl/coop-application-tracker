# Co-op Application Tracker — CSC 370 Sprint 1

Group 3: Amrinder Singh (`amrinder`), Jaiman Singh (`jaiman1`), Aashna Sadeque (`aashnas`). The database tracks job postings, applications, resume selections, interviews and offers. Demo employers, jobs and workflow data are synthetic.

The [progress report and next-sprint plan](SPRINT_PLAN.md) compares this sprint with the kick-off commitments.

## Review the submission

| Evidence | Files |
| --- | --- |
| Conceptual and relational design | [Chen ERD](CONCEPTUAL_ERD.md), [relational ERD](ERD.md), [schema reference](RELATIONAL_SCHEMA.md) |
| Normalization and constraints | [FDs, keys, BCNF, 3NF and 4NF](NORMALIZATION.md), [integrity rules](docs/CONSTRAINTS.md) |
| Course connection | [Competency mapping](docs/COURSE_ALIGNMENT.md), [conceptual-design review](docs/CONCEPTUAL_DESIGN_REVIEW.md), [material inventory](docs/MATERIALS_REVIEW.md) |
| Upgrade from kick-off | [Migration instructions](migrations/README.md), [migration results](evidence/migration-verification.txt) |
| Execution results | [Evidence index](evidence/README.md), [report output](evidence/demo-output.tsv), [clean-copy verification](evidence/clean-export-verification.txt) |
| Recording and submission | [Team script](TEAM_VIDEO_SCRIPT.md), [rehearsal guide](docs/TEAM_REVIEW_GUIDE.md), [checklist](SUBMISSION_CHECKLIST.md), [sources and assistance](SOURCES.md) |

## Create a fresh database

Use Python 3 and MySQL 8.0.16 or later. Verification was run on MySQL 8.4.8. The Python scripts use the standard library. Every new table explicitly uses InnoDB for foreign keys and transactions.

Use a MySQL account that can create databases, tables and triggers and run SELECT/INSERT/UPDATE/DELETE statements. The migration also needs ALTER, CREATE ROUTINE, ALTER ROUTINE and EXECUTE privileges. The [MySQL routine privilege reference](https://dev.mysql.com/doc/refman/8.4/en/stored-routines-privileges.html) explains the routine permissions.

```sh
mysql -u root -p < schema.sql
mysql -u root -p < supporting-files/seed.sql
mysql -u root -p < supporting-files/demo_queries.sql
```

These commands create `coop_application_tracker_sprint1`. Existing tables cause the load to stop; no database is dropped. For a populated kick-off installation, follow the migration instructions instead of loading the new seed over existing data.

## Reproduce the checks

Configure MySQL authentication through `mysql_config_editor` or the client's normal environment, then run:

```sh
python3 scripts/design.py
python3 scripts/verify_theory.py
python3 scripts/conceptual_erd.py
python3 scripts/verify.py
python3 scripts/verify_migration.py
```

The database verifiers create randomly named databases and retain them for inspection. `MYSQL_BIN`, `MYSQL_SOCKET` and `MYSQL_USER` select a different client, socket or account.

The scripts reject `-O` and `PYTHONOPTIMIZE`, which disable their assertions. A failed command is a failed run. The design checker verifies the declared FD model; domain assumptions and MVDs also require the reasoning in NORMALIZATION.md.

After changing the DDL, regenerate both diagrams and the schema reference:

```sh
python3 scripts/design.py --generate
python3 scripts/conceptual_erd.py
```

## Submit

Review the work, record and measure the video, push the final commit to [GitHub](https://github.com/singhamrinder1409-ctrl/coop-application-tracker), and verify instructor/TA access. One member submits the repository URL, exact published commit hash and video in Brightspace.

The original kick-off report is `PROJECT_KICKOFF.md`; its plan, DDL and seed are retained in `docs/archive/`.
