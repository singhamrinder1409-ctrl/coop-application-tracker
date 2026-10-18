# Co-op Application Tracker - CSC 370 Sprint 1

Group 3: Amrinder Singh (`amrinder`), Jaiman Singh (`jaiman1`), Aashna Sadeque (`aashnas`). A MySQL-backed tracker for postings, applications, resume versions, interviews and offers. All demo organizations and job data are synthetic.

Start with the [criterion-by-criterion audit](RUBRIC_AUDIT.md) and [Sprint 1 report and Sprint 2 plan](SPRINT_PLAN.md). They map every kick-off commitment and feedback correction to evidence and states remaining work honestly.

## Submission evidence

- [Chen conceptual ERD](CONCEPTUAL_ERD.md) and [complete relational ERD](ERD.md)
- [All supplied lecture objectives and actual course competencies](docs/COURSE_ALIGNMENT.md)
- [Expanded material audit](docs/UPDATED_MATERIALS_AUDIT.md) and [eight-criterion conceptual-design review](docs/CONCEPTUAL_DESIGN_REVIEW.md)
- [Upgrade from the existing kick-off schema](migrations/README.md), with [migration evidence](evidence/migration-verification.txt)
- [All relation attributes, keys and references](RELATIONAL_SCHEMA.md)
- [FDs, minimal bases, projections, BCNF, 3NF and 4NF](NORMALIZATION.md)
- [Relational algebra constraints and advanced design decisions](docs/CONSTRAINTS.md)
- [Clean export verification](evidence/clean-export-verification.txt)
- [Actual MySQL verification output](evidence/mysql-verification.txt), [design checks](evidence/design-verification.txt), [worked theory examples](evidence/theory-examples.txt), [report results](evidence/demo-output.tsv)
- [Team understanding/rehearsal guide](docs/TEAM_REVIEW_GUIDE.md)
- [Timed team video script](TEAM_VIDEO_SCRIPT.md), [submission checklist](SUBMISSION_CHECKLIST.md), [sources](SOURCES.md)

## Run on MySQL

Requires Python 3 and MySQL 8.0.16+ with InnoDB, CHECK enforcement, CREATE DATABASE/TABLE/TRIGGER privileges; the migration verifier also requires ALTER and CREATE/DROP ROUTINE privileges. Tested with MySQL 8.4.8. No Python packages are required. Do not load the old kick-off seed into the new schema: resume selection is now a separate relation.

```sh
mysql -u root -p < schema.sql
mysql -u root -p < supporting-files/seed.sql
mysql -u root -p < supporting-files/demo_queries.sql
python3 scripts/design.py
python3 scripts/verify_theory.py
python3 scripts/conceptual_erd.py
```

The DDL creates `coop_application_tracker_sprint1`. It does not drop existing data. It will stop on existing tables; use a fresh schema for a fresh load. The kick-off schema is archived. For an existing kick-off installation, follow `migrations/README.md` rather than loading a fresh schema over it.

For reproducible database assertions, configure authentication with `mysql_config_editor` or the MySQL client's normal environment. Then:

```sh
python3 scripts/verify.py
python3 scripts/verify_migration.py
# Optional for a non-default binary/socket:
MYSQL_BIN=/usr/local/mysql/bin/mysql MYSQL_SOCKET=/path/to/mysql.sock python3 scripts/verify.py
MYSQL_BIN=/usr/local/mysql/bin/mysql MYSQL_SOCKET=/path/to/mysql.sock python3 scripts/verify_migration.py
```

The verifier creates a randomly named test database, runs positive/negative and rollback checks, and retains it for inspection. It never deletes a database. An authentication error is a failed run; do not report a pass without seeing the complete output. Use `MYSQL_USER` for a non-root account. Do not commit passwords.

To regenerate ERD/schema documents after DDL changes:

```sh
python3 scripts/design.py --generate
python3 scripts/conceptual_erd.py
```

The FD checker assumes that non-null alternate keys and the documented domain FDs are complete. It does not infer domain truth from sample data or prove 4NF.

## Remaining human submission steps

Confirm full-team consent for AI assistance as required by the Welcome lecture, review the documented design assumptions, record the team video, publish/share this repository, and submit its URL and exact commit hash with the video. No remote is configured in this checkout. See the checklist for commands. Historic kick-off material is retained in `PROJECT_KICKOFF.md` and `docs/archive/`.
