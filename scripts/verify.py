#!/usr/bin/env python3
"""Run against a disposable, freshly named MySQL database. Never drops a database.
MYSQL_BIN and MYSQL_SOCKET select the server. MYSQL_USER defaults to root.
Use mysql_config_editor or MYSQL_PWD for authentication; passwords are not printed.
"""

import os
import re
import subprocess
import uuid
from collections import Counter
from pathlib import Path

if not __debug__:
    raise SystemExit(
        "Verification requires assertions. Run without -O or PYTHONOPTIMIZE."
    )

root = Path(__file__).resolve().parents[1]
db = "coop_sprint1_test_" + uuid.uuid4().hex[:12]
args = [
    os.environ.get("MYSQL_BIN", "mysql"),
    "--batch",
    "--raw",
    "--skip-column-names",
    "-u",
    os.environ.get("MYSQL_USER", "root"),
]
if os.environ.get("MYSQL_SOCKET"):
    args += ["--socket=" + os.environ["MYSQL_SOCKET"]]


def sql(source, database=True):
    return subprocess.run(
        args + ([db] if database else []), input=source, text=True, capture_output=True
    )


def ok(label, statement, expected=None):
    r = sql(statement)
    assert r.returncode == 0, (label, r.stderr)
    if expected is not None:
        assert r.stdout.strip() == expected, (label, r.stdout, expected)
    print("PASS", label)


def reject(label, statement, code):
    r = sql("START TRANSACTION;\n" + statement + ";\nROLLBACK;")
    assert r.returncode != 0 and re.search(r"ERROR " + str(code) + r"\b", r.stderr), (
        label,
        r.stderr,
    )
    print("PASS", label, "(expected MySQL error", str(code) + ")")


print("Disposable database:", db)
r = sql(
    "SET SESSION default_storage_engine=MyISAM;\n"
    + (root / "schema.sql").read_text().replace("coop_application_tracker_sprint1", db),
    False,
)
assert r.returncode == 0, r.stderr
print("PASS DDL loads on MySQL")
r = sql("SELECT VERSION();")
assert r.returncode == 0, r.stderr
print("PASS server version:", r.stdout.strip())
ok(
    "seed loads",
    (root / "supporting-files/seed.sql")
    .read_text()
    .replace("coop_application_tracker_sprint1", db),
)
for name, body in re.findall(
    r"CREATE TABLE (\w+) \((.*?)\n\)(?: ENGINE=InnoDB)?;",
    (root / "schema.sql").read_text(),
    re.S,
):
    declared = re.findall(
        r"^    (\w+) (?:INT|VARCHAR|TEXT|BOOLEAN|DATETIME|DATE|DECIMAL|ENUM)\b",
        body,
        re.M,
    )
    ok(
        "live attribute coverage " + name,
        "SELECT GROUP_CONCAT(column_name ORDER BY ordinal_position) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='"
        + name
        + "'",
        ",".join(declared),
    )
ok(
    "nine tables",
    "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE()",
    "9",
)
ok(
    "explicit InnoDB despite nontransactional session default",
    "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE() AND engine='InnoDB'",
    "9",
)
ok(
    "fixture cardinalities",
    "SELECT (SELECT COUNT(*) FROM Student),(SELECT COUNT(*) FROM Application),(SELECT COUNT(*) FROM Interview),(SELECT COUNT(*) FROM Offer)",
    "4\t6\t2\t2",
)
# Independently specified expected rows test the report file itself, preserving duplicates.
report_source = (root / "supporting-files/demo_queries.sql").read_text()
report_statements = [
    part.strip()
    for part in re.sub(r"--[^\n]*", "", report_source).split(";")
    if part.strip()
]
reports = [part for part in report_statements if part.upper().startswith("SELECT")]
expected_reports = [
    [
        "Amrinder Singh\tOcean Analytics Lab\tData Systems Co-op\t2026-10-04\tinterview\t1",
        "Amrinder Singh\tNorthwind Software\tBackend Developer Co-op\t2026-10-04\tapplied\t2",
        "Jaiman Singh\tNorthwind Software\tBackend Developer Co-op\tNULL\tsaved\t3",
        "Aashna Sadeque\tNorthwind Software\tBackend Developer Co-op\tNULL\tsaved\t3",
        "Aashna Sadeque\tIsland Health Data Team\tHealth Data Analyst Co-op\t2026-10-01\toffer\t4",
        "Jaiman Singh\tOcean Analytics Lab\tData Systems Co-op\tNULL\trejected\t5",
    ],
    [
        "Amrinder Singh\tOcean Analytics Lab\tData Systems Co-op\tinterview",
        "Amrinder Singh\tNorthwind Software\tBackend Developer Co-op\tapplied",
        "Jaiman Singh\tNorthwind Software\tBackend Developer Co-op\tsaved",
        "Aashna Sadeque\tIsland Health Data Team\tHealth Data Analyst Co-op\toffer",
        "Aashna Sadeque\tNorthwind Software\tBackend Developer Co-op\tsaved",
    ],
    [
        "Amrinder Singh\tOcean Analytics Lab\tData Systems Co-op\t2\ttechnical\t2026-10-21 14:00:00\tNULL"
    ],
    ["saved\t2", "applied\t1", "interview\t1", "offer\t1", "rejected\t1"],
    [
        "Aashna Sadeque\tIsland Health Data Team\tHealth Data Analyst Co-op\t28.50\t2026-10-18\t2026-10-25\tpending",
        "Amrinder Singh\tNorthwind Software\tBackend Developer Co-op\t0.00\t2026-10-18\t2026-10-18\tpending",
    ],
    ["Amrinder Singh\t2", "Jaiman Singh\t2", "Aashna Sadeque\t2", "Demo Student\t0"],
    [
        "5\tJaiman Singh\tData Systems Co-op",
        "6\tAashna Sadeque\tBackend Developer Co-op",
    ],
]
assert len(reports) == len(expected_reports) == 7
for number, (statement, expected_rows) in enumerate(zip(reports, expected_reports), 1):
    r = sql(statement + ";")
    assert r.returncode == 0, (number, r.stderr)
    assert Counter(r.stdout.splitlines()) == Counter(expected_rows), (
        number,
        r.stdout,
        expected_rows,
    )
    print(
        "PASS report",
        number,
        "exact expected rows (including duplicate multiplicities)",
    )

ok(
    "upcoming excludes past interview",
    "SELECT interview_round FROM Interview WHERE result='scheduled' AND scheduled_at >= '2026-10-18' ORDER BY interview_round",
    "2",
)
ok(
    "active application set",
    "SELECT GROUP_CONCAT(a.application_id ORDER BY a.application_id) FROM Application a JOIN ApplicationStatus s USING(status_id) WHERE NOT s.is_terminal",
    "1,2,3,4,6",
)
ok(
    "offer boundary values",
    "SELECT COUNT(*) FROM Offer WHERE hourly_wage=0 AND response_deadline=offer_date",
    "1",
)
ok(
    "optional resume absent",
    "SELECT COUNT(*) FROM Application a LEFT JOIN ApplicationResume r USING(application_id) WHERE r.application_id IS NULL",
    "2",
)
ok(
    "student with zero applications",
    "SELECT s.student_id FROM Student s LEFT JOIN Application a USING(student_id) GROUP BY s.student_id HAVING COUNT(a.application_id)=0",
    "4",
)
reject(
    "orphan student",
    "INSERT INTO Application(student_id,posting_id,status_id) VALUES(999,1,1)",
    1452,
)
reject(
    "orphan posting",
    "INSERT INTO Application(student_id,posting_id,status_id) VALUES(4,999,1)",
    1452,
)
reject(
    "orphan status",
    "INSERT INTO Application(student_id,posting_id,status_id) VALUES(4,1,999)",
    1452,
)
reject(
    "missing assignment application",
    "INSERT INTO ApplicationResume VALUES(999,1)",
    1644,
)
reject("missing assignment resume", "INSERT INTO ApplicationResume VALUES(5,999)", 1644)
reject(
    "assigned resume cannot be deleted",
    "DELETE FROM ResumeVersion WHERE resume_id=1",
    1451,
)
reject(
    "duplicate application",
    "INSERT INTO Application(student_id,posting_id,status_id) VALUES(1,1,1)",
    1062,
)
reject(
    "priority lower bound",
    "UPDATE Application SET priority=0 WHERE application_id=1",
    3819,
)
reject(
    "priority upper bound",
    "UPDATE Application SET priority=6 WHERE application_id=1",
    3819,
)
reject(
    "NULL priority", "UPDATE Application SET priority=NULL WHERE application_id=1", 1048
)
reject(
    "posting date order",
    "UPDATE JobPosting SET application_deadline='2026-01-01' WHERE posting_id=1",
    3819,
)
reject(
    "resume version positive",
    "UPDATE ResumeVersion SET version_number=0 WHERE resume_id=1",
    3819,
)
reject(
    "duplicate resume version",
    "UPDATE ResumeVersion SET version_number=1 WHERE resume_id=2",
    1062,
)
reject(
    "interview round positive",
    "UPDATE Interview SET interview_round=0 WHERE interview_id=1",
    3819,
)
reject(
    "duplicate interview round",
    "UPDATE Interview SET interview_round=1 WHERE interview_id=2",
    1062,
)
reject("negative wage", "UPDATE Offer SET hourly_wage=-1 WHERE offer_id=1", 3819)
reject(
    "offer deadline order",
    "UPDATE Offer SET response_deadline='2026-01-01' WHERE offer_id=1",
    3819,
)
reject(
    "one offer per application",
    "INSERT INTO Offer(application_id,offer_date) VALUES(4,'2026-10-18')",
    1062,
)
reject(
    "boolean domain",
    "UPDATE ApplicationStatus SET is_terminal=2 WHERE status_id=1",
    3819,
)
reject("resume ownership insert", "INSERT INTO ApplicationResume VALUES(5,1)", 1644)
reject(
    "resume ownership update",
    "UPDATE ApplicationResume SET resume_id=3 WHERE application_id=1",
    1644,
)
reject(
    "association application update",
    "UPDATE ApplicationResume SET application_id=5 WHERE application_id=1",
    1644,
)
reject(
    "application owner immutable",
    "UPDATE Application SET student_id=2 WHERE application_id=1",
    1644,
)
reject(
    "resume owner immutable",
    "UPDATE ResumeVersion SET student_id=2 WHERE resume_id=1",
    1644,
)
reject(
    "referenced student cannot be deleted",
    "DELETE FROM Student WHERE student_id=1",
    1451,
)
ok(
    "ownership algebra invariant",
    "SELECT COUNT(*) FROM Application a JOIN ApplicationResume ar ON ar.application_id=a.application_id JOIN ResumeVersion r ON r.resume_id=ar.resume_id WHERE a.student_id <> r.student_id",
    "0",
)
ok(
    "valid resume replacement rolls back",
    "START TRANSACTION; UPDATE ApplicationResume SET resume_id=2 WHERE application_id=1; SELECT resume_id FROM ApplicationResume WHERE application_id=1; ROLLBACK;",
    "2",
)
ok(
    "workflow create apply interview offer then rollback",
    """START TRANSACTION;
INSERT INTO Application(student_id,posting_id,status_id,date_applied) VALUES(4,1,2,'2026-10-18');
SET @app=LAST_INSERT_ID();
INSERT INTO ResumeVersion(student_id,resume_label,version_number,created_on) VALUES(4,'Demo',1,'2026-10-18');
INSERT INTO ApplicationResume VALUES(@app,LAST_INSERT_ID());
INSERT INTO Interview(application_id,interview_round,interview_type,scheduled_at) VALUES(@app,1,'video','2026-10-20');
UPDATE Application SET status_id=4 WHERE application_id=@app;
INSERT INTO Offer(application_id,offer_date,hourly_wage) VALUES(@app,'2026-10-21',30);
SELECT COUNT(*) FROM Application a JOIN ApplicationResume r USING(application_id) JOIN Interview i USING(application_id) JOIN Offer o USING(application_id) WHERE a.application_id=@app;
ROLLBACK;""",
    "1",
)
ok("rollback restores six applications", "SELECT COUNT(*) FROM Application", "6")
print("ALL DATABASE CHECKS PASSED; retained database for inspection:", db)
