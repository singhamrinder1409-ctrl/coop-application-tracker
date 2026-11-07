#!/usr/bin/env python3
"""Check Sprint 2 on a fresh database, retaining it for inspection.

Uses the same MYSQL_BIN, MYSQL_SOCKET and MYSQL_USER settings as verify.py.
Optional --output-dir writes report TSVs and a log only after every check passes.
"""

import argparse
import os
import re
import subprocess
import uuid
from pathlib import Path

if not __debug__:
    raise SystemExit(
        "Verification requires assertions. Run without -O or PYTHONOPTIMIZE."
    )

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output-dir", type=Path)
options = parser.parse_args()
db = "coop_sprint2_test_" + uuid.uuid4().hex[:12]
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
log = []
outputs = {}


def say(message):
    print(message, flush=True)
    log.append(message)


def sql(source, use_db=True):
    return subprocess.run(
        args + ([db] if use_db else []), input=source, text=True, capture_output=True
    )


def execute(source, use_db=True):
    result = sql(source, use_db)
    assert result.returncode == 0, result.stderr
    return result.stdout


def load(path, use_db=True):
    return execute(
        (root / path).read_text().replace("coop_application_tracker_sprint1", db),
        use_db,
    )


def rows(source):
    return [tuple(line.split("\t")) for line in execute(source).splitlines()]


def expected_rows(values):
    return [tuple("NULL" if v is None else str(v) for v in row) for row in values]


def check(label, statement, expected, before="", after=""):
    result = rows(before + "\n" + statement + ";\n" + after)
    want = expected_rows(expected)
    assert result == want, (label, result, want)
    say("PASS " + label)
    return result


def named_queries(filename):
    source = (root / "supporting-files/sprint2" / filename).read_text()
    parts = re.split(r"^-- name: (\w+)\s*$", source, flags=re.M)
    assert len(parts) > 1, filename
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def reject(label, statement, code, text):
    result = sql(statement)
    assert result.returncode != 0, (label, "unexpected success")
    assert re.search(r"ERROR " + str(code) + r"\b", result.stderr), (
        label,
        result.stderr,
    )
    assert text in result.stderr, (label, result.stderr)
    say(f"PASS {label} (expected MySQL error {code})")


say("Disposable database: " + db)
say("Version: " + execute("SELECT VERSION();", False).strip())
load("schema.sql", False)
load("supporting-files/seed.sql")
load("supporting-files/sprint2/views.sql")
load("supporting-files/sprint2/transactions.sql")
check(
    "nine unchanged base tables and two views",
    "SELECT table_type, COUNT(*) FROM information_schema.tables "
    "WHERE table_schema=DATABASE() GROUP BY table_type ORDER BY table_type",
    [("BASE TABLE", 9), ("VIEW", 2)],
)

headers = {
    "R1": "student_id full_name application_count active_application_count interviewed_application_count offered_application_count",
    "R2": "employer_id employer_name application_count",
    "R3": "application_id student_id priority",
    "R4": "student_id full_name",
    "R5": "application_id student_id",
    "R6": "student_id",
    "R7": "status_id status_name application_count",
    "R8": "student_id full_name",
    "O1": "status_id status_name application_count percent_of_applications",
    "O2": "student_id application_id priority priority_rank",
}
reports = named_queries("reports.sql")
optional = named_queries("optional_reports.sql")
pairs = named_queries("equivalence.sql")
# Expected rows are hand-derived from the fixed seed, not calculated by the reports.
workload = [
    (1, "Amrinder Singh", 2, 2, 1, 1),
    (2, "Jaiman Singh", 2, 1, 0, 0),
    (3, "Aashna Sadeque", 2, 2, 0, 1),
    (4, "Demo Student", 0, 0, 0, 0),
]
report_expected = {
    "R1": workload,
    "R2": [(1, "Ocean Analytics Lab", 2), (2, "Northwind Software", 3)],
    "R3": [(2, 1, 2), (4, 3, 4), (5, 2, 5)],
    "R4": [(2, "Jaiman Singh"), (3, "Aashna Sadeque"), (4, "Demo Student")],
    "R5": [(5, 2), (6, 3)],
    "R6": [(2,), (3,), (4,)],
    "R7": [
        (1, "saved", 2),
        (2, "applied", 1),
        (3, "interview", 1),
        (4, "offer", 1),
        (5, "rejected", 1),
        (6, "withdrawn", 0),
    ],
    "R8": [(1, "Amrinder Singh")],
}
assert set(reports) == set(report_expected)
for name, query in reports.items():
    actual = check(name + " exact ordered report rows", query, report_expected[name])
    outputs[name + ".tsv"] = (
        "\t".join(headers[name].split())
        + "\n"
        + "\n".join("\t".join(row) for row in actual)
        + "\n"
    )

app_projection = (
    "SELECT application_id, student_id, posting_id, employer_id, status_name, "
    "is_terminal, priority, resume_id, interview_count, offer_id "
    "FROM ApplicationOverview ORDER BY application_id"
)
apps = [
    (1, 1, 1, 1, "interview", 0, 1, 1, 2, None),
    (2, 1, 2, 2, "applied", 0, 2, 2, 0, 2),
    (3, 2, 2, 2, "saved", 0, 3, 3, 0, None),
    (4, 3, 3, 3, "offer", 0, 4, 4, 0, 1),
    (5, 2, 1, 1, "rejected", 1, 5, None, 0, None),
    (6, 3, 2, 2, "saved", 0, 3, None, 0, None),
]
check("ApplicationOverview independent expected rows", app_projection, apps)
direct_app = """SELECT a.application_id, a.student_id, s.full_name, a.posting_id,
 p.job_title, e.employer_id, e.employer_name, st.status_name, st.is_terminal,
 a.priority, ar.resume_id,
 (SELECT COUNT(*) FROM Interview i WHERE i.application_id=a.application_id), o.offer_id
 FROM Application a JOIN Student s ON s.student_id=a.student_id
 JOIN JobPosting p ON p.posting_id=a.posting_id
 JOIN Employer e ON e.employer_id=p.employer_id
 JOIN ApplicationStatus st ON st.status_id=a.status_id
 LEFT JOIN ApplicationResume ar ON ar.application_id=a.application_id
 LEFT JOIN Offer o ON o.application_id=a.application_id ORDER BY a.application_id"""
assert rows(direct_app) == rows(
    "SELECT * FROM ApplicationOverview ORDER BY application_id"
)
say("PASS ApplicationOverview all columns equal direct query")
direct_student = """SELECT s.student_id, s.full_name,
 (SELECT COUNT(*) FROM Application a WHERE a.student_id=s.student_id),
 (SELECT COUNT(*) FROM Application a JOIN ApplicationStatus st ON st.status_id=a.status_id
  WHERE a.student_id=s.student_id AND st.is_terminal=0),
 (SELECT COUNT(*) FROM Application a WHERE a.student_id=s.student_id
  AND EXISTS (SELECT 1 FROM Interview i WHERE i.application_id=a.application_id)),
 (SELECT COUNT(*) FROM Offer o JOIN Application a ON a.application_id=o.application_id
  WHERE a.student_id=s.student_id)
 FROM Student s ORDER BY s.student_id"""
check(
    "StudentWorkload direct-query equivalence with expected rows",
    direct_student,
    workload,
)

pair_expected = {
    "E1": [(5,), (6,)],
    "E2": [(1, 2), (2, 2), (3, 2), (4, 0)],
    "E3": [(1,)],
    "E4": [(1,), (2,), (5,), (6,)],
}


def compare_pair(name, expected, before="", after="", scenario="baseline"):
    # Each formulation runs in its own connection with the same rolled-back fixture.
    check(
        name + " " + scenario + " A expected bag",
        pairs[name + "A"],
        expected,
        before,
        after,
    )
    check(
        name + " " + scenario + " B expected bag",
        pairs[name + "B"],
        expected,
        before,
        after,
    )


for name, expected in pair_expected.items():
    compare_pair(name, expected)
compare_pair(
    "E1",
    [(1,), (2,), (3,), (4,), (5,), (6,)],
    "START TRANSACTION; DELETE FROM ApplicationResume;",
    "ROLLBACK;",
    "no assignments",
)
compare_pair(
    "E2",
    [(1, 2), (2, 2), (3, 2), (4, 0), (5, 0)],
    "START TRANSACTION; INSERT INTO Student(student_id,full_name,username) "
    "VALUES(5,'Demo Student','another_demo');",
    "ROLLBACK;",
    "duplicate display names",
)
compare_pair(
    "E3", [], "START TRANSACTION; DELETE FROM Interview;", "ROLLBACK;", "no interviews"
)
compare_pair(
    "E4",
    pair_expected["E4"],
    "START TRANSACTION; UPDATE Application SET source=NULL WHERE application_id=1;",
    "ROLLBACK;",
    "overlapping branches",
)
check(
    "UNION ALL overlap would duplicate application 1",
    pairs["E4A"].replace("UNION", "UNION ALL"),
    [(1,), (1,), (2,), (5,), (6,)],
    "START TRANSACTION; UPDATE Application SET source=NULL WHERE application_id=1;",
    "ROLLBACK;",
)
check(
    "NOT IN with a NULL right side loses the no-application student",
    "SELECT student_id FROM Student WHERE student_id NOT IN "
    "(SELECT student_id FROM Application UNION SELECT NULL) ORDER BY student_id",
    [],
)
check(
    "NOT EXISTS keeps the no-application student",
    "SELECT s.student_id FROM Student s WHERE NOT EXISTS "
    "(SELECT 1 FROM Application a WHERE a.student_id=s.student_id) ORDER BY s.student_id",
    [(4,)],
)
check(
    "COUNT star would report one application for the unmatched student",
    "SELECT s.student_id, COUNT(*) FROM Student s LEFT JOIN Application a "
    "ON a.student_id=s.student_id WHERE s.student_id=4 GROUP BY s.student_id",
    [(4, 1)],
)
check(
    "join without DISTINCT duplicates the interviewed application",
    pairs["E3B"].replace("SELECT DISTINCT", "SELECT"),
    [(1,), (1,)],
)
check(
    "extra interview does not multiply offered/interviewed applications",
    reports["R1"],
    workload,
    "START TRANSACTION; INSERT INTO Interview(application_id,interview_round,interview_type,scheduled_at) "
    "VALUES(1,3,'video','2026-11-10 09:00:00');",
    "ROLLBACK;",
)
check(
    "distinct student IDs preserve duplicate display names",
    reports["R1"],
    workload + [(5, "Demo Student", 0, 0, 0, 0)],
    "START TRANSACTION; INSERT INTO Student(student_id,full_name,username) "
    "VALUES(5,'Demo Student','another_demo');",
    "ROLLBACK;",
)
check(
    "division on an empty open-posting set includes all students",
    reports["R8"],
    [
        (1, "Amrinder Singh"),
        (2, "Jaiman Singh"),
        (3, "Aashna Sadeque"),
        (4, "Demo Student"),
    ],
    "START TRANSACTION; UPDATE JobPosting SET posting_status='closed';",
    "ROLLBACK;",
)
check(
    "new open posting without applications makes division empty",
    reports["R8"],
    [],
    "START TRANSACTION; INSERT INTO JobPosting(employer_id,job_title,work_term) "
    "VALUES(1,'Unfilled role','Spring 2027');",
    "ROLLBACK;",
)
check(
    "offer count includes offers with NULL wage",
    reports["R1"],
    workload,
    "START TRANSACTION; UPDATE Offer SET hourly_wage=NULL WHERE offer_id=2;",
    "ROLLBACK;",
)

ranks = [
    (1, 1, 1, 1),
    (1, 2, 2, 2),
    (2, 3, 3, 1),
    (2, 5, 5, 2),
    (3, 6, 3, 1),
    (3, 4, 4, 2),
]
optional_expected = {
    "O1": [
        (1, "saved", 2, "33.33"),
        (2, "applied", 1, "16.67"),
        (3, "interview", 1, "16.67"),
        (4, "offer", 1, "16.67"),
        (5, "rejected", 1, "16.67"),
        (6, "withdrawn", 0, "0.00"),
    ],
    "O2": ranks,
}
assert set(optional) == set(optional_expected)
for name, query in optional.items():
    actual = check(
        name + " optional CTE/window report expected rows",
        query,
        optional_expected[name],
    )
    outputs[name + ".tsv"] = (
        "\t".join(headers[name].split())
        + "\n"
        + "\n".join("\t".join(row) for row in actual)
        + "\n"
    )
check(
    "window tie broken by posting/application IDs",
    optional["O2"],
    [(1, 1, 1, 1), (1, 2, 1, 2)] + ranks[2:],
    "START TRANSACTION; UPDATE Application SET priority=1 WHERE application_id=2;",
    "ROLLBACK;",
)
empty = (
    "START TRANSACTION; DELETE FROM Offer; DELETE FROM Interview; "
    "DELETE FROM ApplicationResume; DELETE FROM Application;"
)
compare_pair(
    "E2", [(1, 0), (2, 0), (3, 0), (4, 0)], empty, "ROLLBACK;", "no applications"
)
check(
    "CTE empty fixture avoids division by zero",
    optional["O1"],
    [
        (1, "saved", 0, "0.00"),
        (2, "applied", 0, "0.00"),
        (3, "interview", 0, "0.00"),
        (4, "offer", 0, "0.00"),
        (5, "rejected", 0, "0.00"),
        (6, "withdrawn", 0, "0.00"),
    ],
    empty,
    "ROLLBACK;",
)
check("window empty fixture returns no rows", optional["O2"], [], empty, "ROLLBACK;")

# Call on standalone connections. Each check afterward uses a new mysql process.
execute(
    "INSERT INTO Interview(application_id,interview_round,interview_type,scheduled_at) "
    "VALUES(2,1,'phone','2026-11-09 09:00:00');"
)
reject(
    "duplicate round after status update triggers rollback",
    "CALL ScheduleInterview(2,1,'video','2026-11-10 10:00:00');",
    1062,
    "Duplicate entry",
)
check(
    "failed duplicate preserves old status and interview count in new connection",
    "SELECT a.status_id, COUNT(i.interview_id) FROM Application a "
    "LEFT JOIN Interview i ON i.application_id=a.application_id "
    "WHERE a.application_id=2 GROUP BY a.status_id",
    [(2, 1)],
)
reject(
    "NULL schedule after status update triggers rollback",
    "CALL ScheduleInterview(6,1,'video',NULL);",
    1048,
    "cannot be null",
)
check(
    "failed NULL schedule preserves saved status and no child",
    "SELECT a.status_id, COUNT(i.interview_id) FROM Application a "
    "LEFT JOIN Interview i ON i.application_id=a.application_id "
    "WHERE a.application_id=6 GROUP BY a.status_id",
    [(1, 0)],
)
reject(
    "nonpositive round rejected",
    "CALL ScheduleInterview(6,0,'video','2026-11-10');",
    3819,
    "Check constraint",
)
check(
    "failed round check rolls status back",
    "SELECT status_id FROM Application WHERE application_id=6",
    [(1,)],
)
reject(
    "unknown application rejected",
    "CALL ScheduleInterview(999,1,'video','2026-11-10');",
    1644,
    "Application does not exist",
)
reject(
    "terminal application rejected",
    "CALL ScheduleInterview(5,1,'video','2026-11-10');",
    1644,
    "Cannot schedule a terminal application",
)
reject(
    "invalid interview type rejected",
    "CALL ScheduleInterview(6,1,'fax','2026-11-10');",
    1644,
    "Invalid interview type",
)
reject(
    "autocommit-disabled caller rejected",
    "SET autocommit=0; CALL ScheduleInterview(6,1,'video','2026-11-10');",
    1644,
    "Use a standalone autocommit connection",
)
execute("UPDATE ApplicationStatus SET is_terminal=1 WHERE status_name='interview';")
reject(
    "unusable interview status rejected",
    "CALL ScheduleInterview(6,1,'video','2026-11-10');",
    1644,
    "Interview status is missing or terminal",
)
execute("UPDATE ApplicationStatus SET is_terminal=0 WHERE status_name='interview';")
execute("CALL ScheduleInterview(3,1,'technical','2026-11-10 14:00:00');")
check(
    "committed status and interview visible in new connection",
    "SELECT a.application_id, a.status_id, i.interview_round, i.interview_type, i.scheduled_at "
    "FROM Application a JOIN Interview i ON i.application_id=a.application_id WHERE a.application_id=3",
    [(3, 3, 1, "technical", "2026-11-10 14:00:00")],
)
reject(
    "ownership enforcement remains active",
    "UPDATE ApplicationResume SET resume_id=3 WHERE application_id=1;",
    1644,
    "Resume must belong to application student",
)
check(
    "still nine base tables after routine workflow",
    "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE() AND table_type='BASE TABLE'",
    [(9,)],
)
say(
    f"ALL SPRINT 2 CHECKS PASSED ({sum(line.startswith('PASS ') for line in log)} checks)."
)
say("Retained disposable database: " + db)
if options.output_dir:
    options.output_dir.mkdir(parents=True, exist_ok=True)
    for name, content in outputs.items():
        (options.output_dir / name).write_text(content)
    (options.output_dir / "verification.txt").write_text("\n".join(log) + "\n")
