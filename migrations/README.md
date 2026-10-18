# Upgrade the existing kick-off schema

The current project extends the same Co-op Application Tracker. `001_sprint1.sql` upgrades the exact original eight-table DDL archived at `docs/archive/KICKOFF_SCHEMA.sql`. The old seed is preserved beside it. It retains student/application data and moves each existing non-NULL resume selection to ApplicationResume before dropping the old resume column.

For a new installation use the root `schema.sql` and current seed. For an existing installation, stop application writers for the upgrade, back up the database and inspect `SHOW CREATE TABLE Application` first. The migration expects database `coop_application_tracker`, the original FK name `Application_ibfk_4`, and no existing ApplicationResume table. Adapt those identifiers if the installed kick-off DDL differs. Do not load the current seed over existing data.

```sh
mysql -u root -p < migrations/001_sprint1.sql
```

Use the normal mysql client without `--force`: it must stop on errors. A preflight rejects cross-student resume selections, NULL priorities and invalid terminal booleans before table changes. Correct the reported data issue explicitly and retry. MySQL DDL commits implicitly: this migration is not an atomic transaction, and failures after preflight require inspection/recovery from backup rather than blind reruns. It never drops a database.

`python3 scripts/verify_migration.py` proves the migration on the archived kick-off fixture, including an invalid ownership preflight and preservation of every original assignment. Actual results are in `evidence/migration-verification.txt`. Verification uses fresh random schemas on an isolated server; the user's existing databases and Desktop copy have not been migrated.
