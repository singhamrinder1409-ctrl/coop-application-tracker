# Sprint 2 execution evidence

These results are produced by `scripts/verify_sprint2.py` and the original five verifiers. The Sprint 2 test uses a fresh randomly named database, loads the unchanged schema/seed and installs the new views and procedure. The base fixture has four students and six applications. Extra edge fixtures run in rollback transactions; the final procedure tests change only the disposable database.

| File | Contents |
| --- | --- |
| `verification.txt` | Sprint 2 checks: exact report results, view/direct-query checks, four equivalence pairs on normal and edge data, bag/NULL counterexamples, optional reports, rollback and committed-read tests |
| `regression.txt` | Environment, clean-copy verification of all six commands, original-suite results and optimized-mode rejection checks |
| `R1.tsv` | Student workload including zero applications |
| `R2.tsv` | Employers with at least two applications in the specified work term |
| `R3.tsv` | Applications with priority numerically above their student's mean |
| `R4.tsv` | Students with no interviews |
| `R5.tsv` | Applications with no selected resume |
| `R6.tsv` | UNION of students missing a resume choice and students with no applications |
| `R7.tsv` | Every status label and its application count |
| `R8.tsv` | Students who actually applied to every open posting |
| `O1.tsv` | Optional CTE current-status counts and percentages |
| `O2.tsv` | Optional ROW_NUMBER ranking per student |

The TSV files include headers and come from the fixed seed before test-only workflow changes. Read the [SQL explanation](../../docs/ADVANCED_SQL.md) for expected results and empty-set rules. Current correctness checks do not establish large-scale performance, complete crash recovery, every concurrent schedule or group submission status.

Reproduce with the commands in the root README. `--output-dir PATH` writes report exports and the Sprint 2 log only after every Sprint 2 check passes. Authentication uses the MySQL client's settings; MYSQL_BIN, MYSQL_SOCKET and MYSQL_USER select the client/server/account. The tests retain their randomly named databases and do not drop an existing database. The historical reset statement in the archived kickoff schema is stripped by the migration verifier.
