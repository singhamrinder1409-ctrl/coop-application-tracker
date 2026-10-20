# Actual Sprint 1 execution evidence

Run date: 2026-10-18, America/Vancouver. Environment: macOS arm64, MySQL Community Server 8.4.8. Verification used an isolated server with networking disabled; existing application databases were not altered. Test data is synthetic. Video and publication are separate submission steps.

- `mysql-verification.txt`: 56 passing checks, including explicit InnoDB under a MyISAM session default, schema load and all live columns, fixture cardinalities, seven reports compared with independent expected rows, valid workflow, rollback, and expected rejected writes. Negative checks require specific MySQL error codes.
- `design-verification.txt`: nine relations checked for candidate keys, minimal FD bases and BCNF under declared assumptions; ERD coverage, projected FD and lossless-intersection checks.
- `theory-examples.txt`: 12 passing worked-example checks for minimal bases, complete FD projection, losslessness/preservation, 3NF versus BCNF, lost dependency enforcement, a full 3NF synthesis with key augmentation, formal MVD rules, and a 4NF decomposition.
- `migration-verification.txt`: 15 passing checks on the archived kick-off schema, ownership/engine preflight rejection and preservation of all original assignments.
- `conceptual-erd-verification.txt`: Chen descriptive-attribute coverage and mapping of all SQL FK columns through relationships.
- `demo-output.tsv`: actual output from the seven supplied report queries on the same successful test database. Upcoming interviews use 2026-10-18 as a fixed demonstration date.

The automated verification tools and optional migration implementation are retained locally, outside the submission checkout. These logs record the completed development runs; the automated suites cannot be rerun using this checkout alone. The supplied schema, seed and report SQL reproduce the database demonstration. See the root README for commands.

The 4NF discussion is a domain/MVD argument, not an automated FD test result. Course mappings and technical limits are recorded in SPRINT_PLAN.md. Recording, recipient access and Brightspace upload are separate submission actions.
