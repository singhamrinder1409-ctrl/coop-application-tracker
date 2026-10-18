# Actual Sprint 1 execution evidence

Run date: 2026-10-18, America/Vancouver. Environment: macOS arm64, MySQL Community Server 8.4.8. Verification used an isolated server with networking disabled; the user's existing MySQL databases were not altered. Test data is synthetic. No UI, video, TA interview or public repository is implied by these records.

- `mysql-verification.txt`: 43 passing checks, including schema load, all live columns, fixture cardinalities, reports, valid workflow, rollback, and expected rejected writes. Negative checks require specific MySQL error codes.
- `design-verification.txt`: nine relations checked for candidate keys, minimal FD bases and BCNF under declared assumptions; ERD coverage, projected FD and lossless-intersection checks.
- `demo-output.tsv`: actual output from the five supplied report queries on the same successful test database. Upcoming interviews use 2026-10-18 as a fixed demonstration date.

Reproduce with Python 3 and a suitably privileged MySQL client:

```sh
python3 scripts/design.py
python3 scripts/verify.py
```

`MYSQL_BIN`, `MYSQL_SOCKET` and `MYSQL_USER` customize the client. The verifier creates a fresh random database and retains it; it never drops an existing database. See the root README for authentication/setup. Test database names in the log are generated run identifiers, not credentials. Test stdout was saved after successful completion; a failed partial output must never be treated as complete evidence.

The 4NF discussion is a domain/MVD argument, not an automated FD test result. The competency mapping uses the assignment and feedback, as the group confirmed no separate list or additional TA requirements exist. A live TA review has not occurred and remains disclosed in SPRINT_PLAN.md.
