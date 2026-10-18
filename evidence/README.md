# Actual Sprint 1 execution evidence

Run date: 2026-10-18, America/Vancouver. Environment: macOS arm64, MySQL Community Server 8.4.8. Verification used an isolated server with networking disabled; the user's existing MySQL databases were not altered. Test data is synthetic. Video and publication are separate submission steps.

- `clean-export-verification.txt`: all five verification commands passed from a clean copy of tracked/non-ignored project files without .git or virtualenv dependencies.
- `verification-safety.txt`: ten checks confirming that each CLI rejects -O and PYTHONOPTIMIZE before printing a pass.
- `mysql-verification.txt`: 56 passing checks, including explicit InnoDB under a MyISAM session default, schema load and all live columns, fixture cardinalities, seven reports compared with independent expected rows, valid workflow, rollback, and expected rejected writes. Negative checks require specific MySQL error codes.
- `design-verification.txt`: nine relations checked for candidate keys, minimal FD bases and BCNF under declared assumptions; ERD coverage, projected FD and lossless-intersection checks.
- `theory-examples.txt`: 12 passing worked-example checks for minimal bases, complete FD projection, losslessness/preservation, 3NF versus BCNF, lost dependency enforcement, a full 3NF synthesis with key augmentation, formal MVD rules, and a 4NF decomposition.
- `migration-verification.txt`: 15 passing checks on the archived kick-off schema, ownership/engine preflight rejection and preservation of all original assignments.
- `conceptual-erd-verification.txt`: Chen descriptive-attribute coverage and mapping of all SQL FK columns through relationships.
- `demo-output.tsv`: actual output from the seven supplied report queries on the same successful test database. Upcoming interviews use 2026-10-18 as a fixed demonstration date.

Reproduce with Python 3 and a suitably privileged MySQL client:

```sh
python3 scripts/design.py
python3 scripts/verify_theory.py
python3 scripts/conceptual_erd.py
python3 scripts/verify.py
python3 scripts/verify_migration.py
```

`MYSQL_BIN`, `MYSQL_SOCKET` and `MYSQL_USER` customize the client. The verifier creates a fresh random database and retains it; it never drops an existing database. See the root README for authentication/setup. Test database names in the log are generated run identifiers, not credentials. Test stdout was saved after successful completion; a failed partial output must never be treated as complete evidence.

The 4NF discussion is a domain/MVD argument, not an automated FD test result. Course mappings and remaining submission actions are recorded in the report and checklist.
