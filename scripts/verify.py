#!/usr/bin/env python3
"""Run against a disposable, freshly named MySQL database. Never drops a database.
MYSQL_BIN and MYSQL_SOCKET select the server. MYSQL_USER defaults to root.
Use mysql_config_editor or MYSQL_PWD for authentication; passwords are not printed.
"""
import os, subprocess, re, sys, uuid
from pathlib import Path
root = Path(__file__).resolve().parents[1]
db = 'coop_sprint1_test_' + uuid.uuid4().hex[:12]
args = [os.environ.get('MYSQL_BIN', 'mysql'), '--batch', '--raw', '--skip-column-names', '-u', os.environ.get('MYSQL_USER','root')]
if os.environ.get('MYSQL_SOCKET'): args += ['--socket=' + os.environ['MYSQL_SOCKET']]

def sql(source, database=True):
    return subprocess.run(args + ([db] if database else []), input=source, text=True, capture_output=True)

def ok(label, statement, expected=None):
    r=sql(statement)
    assert r.returncode == 0, (label,r.stderr)
    if expected is not None: assert r.stdout.strip()==expected, (label, r.stdout, expected)
    print('PASS',label)

def reject(label, statement, code):
    r=sql('START TRANSACTION;\n'+statement+';\nROLLBACK;')
    assert r.returncode != 0 and re.search(r'ERROR '+str(code)+r'\b',r.stderr), (label,r.stderr)
    print('PASS',label,'(expected MySQL error',str(code)+')')

print('Disposable database:',db)
r=sql((root/'schema.sql').read_text().replace('coop_application_tracker_sprint1',db),False)
assert r.returncode==0,r.stderr
print('PASS DDL loads on MySQL')
r=sql('SELECT VERSION();'); assert r.returncode == 0, r.stderr
print('PASS server version:',r.stdout.strip())
ok('seed loads', (root/'supporting-files/seed.sql').read_text().replace('coop_application_tracker_sprint1',db))
for name,body in re.findall(r'CREATE TABLE (\w+) \((.*?)\n\);', (root/'schema.sql').read_text(), re.S):
    declared=re.findall(r'^    (\w+) (?:INT|VARCHAR|TEXT|BOOLEAN|DATETIME|DATE|DECIMAL|ENUM)\b',body,re.M)
    ok('live attribute coverage '+name, "SELECT GROUP_CONCAT(column_name ORDER BY ordinal_position) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='"+name+"'", ','.join(declared))
ok('nine tables', 'SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE()', '9')
ok('fixture cardinalities', 'SELECT (SELECT COUNT(*) FROM Student),(SELECT COUNT(*) FROM Application),(SELECT COUNT(*) FROM Interview),(SELECT COUNT(*) FROM Offer)', '4\t6\t2\t2')
ok('five reporting queries execute', (root/'supporting-files/demo_queries.sql').read_text().replace('coop_application_tracker_sprint1',db))
ok('upcoming excludes past interview', "SELECT interview_round FROM Interview WHERE result='scheduled' AND scheduled_at >= '2026-10-18' ORDER BY interview_round", '2')
ok('active application set', 'SELECT GROUP_CONCAT(a.application_id ORDER BY a.application_id) FROM Application a JOIN ApplicationStatus s USING(status_id) WHERE NOT s.is_terminal','1,2,3,4,6')
ok('offer boundary values', 'SELECT COUNT(*) FROM Offer WHERE hourly_wage=0 AND response_deadline=offer_date','1')
ok('optional resume absent', 'SELECT COUNT(*) FROM Application a LEFT JOIN ApplicationResume r USING(application_id) WHERE r.application_id IS NULL','2')
ok('student with zero applications', 'SELECT s.student_id FROM Student s LEFT JOIN Application a USING(student_id) GROUP BY s.student_id HAVING COUNT(a.application_id)=0','4')
reject('orphan student', 'INSERT INTO Application(student_id,posting_id,status_id) VALUES(999,1,1)',1452)
reject('duplicate application', 'INSERT INTO Application(student_id,posting_id,status_id) VALUES(1,1,1)',1062)
reject('priority lower bound','UPDATE Application SET priority=0 WHERE application_id=1',3819)
reject('priority upper bound','UPDATE Application SET priority=6 WHERE application_id=1',3819)
reject('NULL priority','UPDATE Application SET priority=NULL WHERE application_id=1',1048)
reject('posting date order', "UPDATE JobPosting SET application_deadline='2026-01-01' WHERE posting_id=1",3819)
reject('resume version positive','UPDATE ResumeVersion SET version_number=0 WHERE resume_id=1',3819)
reject('duplicate resume version','UPDATE ResumeVersion SET version_number=1 WHERE resume_id=2',1062)
reject('interview round positive','UPDATE Interview SET interview_round=0 WHERE interview_id=1',3819)
reject('duplicate interview round','UPDATE Interview SET interview_round=1 WHERE interview_id=2',1062)
reject('negative wage','UPDATE Offer SET hourly_wage=-1 WHERE offer_id=1',3819)
reject('offer deadline order', "UPDATE Offer SET response_deadline='2026-01-01' WHERE offer_id=1",3819)
reject('one offer per application', "INSERT INTO Offer(application_id,offer_date) VALUES(4,'2026-10-18')",1062)
reject('boolean domain','UPDATE ApplicationStatus SET is_terminal=2 WHERE status_id=1',3819)
reject('resume ownership insert','INSERT INTO ApplicationResume VALUES(5,1)',1644)
reject('resume ownership update','UPDATE ApplicationResume SET resume_id=3 WHERE application_id=1',1644)
reject('association application update','UPDATE ApplicationResume SET application_id=5 WHERE application_id=1',1644)
reject('application owner immutable','UPDATE Application SET student_id=2 WHERE application_id=1',1644)
reject('resume owner immutable','UPDATE ResumeVersion SET student_id=2 WHERE resume_id=1',1644)
reject('referenced student cannot be deleted','DELETE FROM Student WHERE student_id=1',1451)
ok('valid resume replacement rolls back','START TRANSACTION; UPDATE ApplicationResume SET resume_id=2 WHERE application_id=1; SELECT resume_id FROM ApplicationResume WHERE application_id=1; ROLLBACK;', '2')
ok('workflow create apply interview offer then rollback', """START TRANSACTION;
INSERT INTO Application(student_id,posting_id,status_id,date_applied) VALUES(4,1,2,'2026-10-18');
SET @app=LAST_INSERT_ID();
INSERT INTO ResumeVersion(student_id,resume_label,version_number,created_on) VALUES(4,'Demo',1,'2026-10-18');
INSERT INTO ApplicationResume VALUES(@app,LAST_INSERT_ID());
INSERT INTO Interview(application_id,interview_round,interview_type,scheduled_at) VALUES(@app,1,'video','2026-10-20');
UPDATE Application SET status_id=4 WHERE application_id=@app;
INSERT INTO Offer(application_id,offer_date,hourly_wage) VALUES(@app,'2026-10-21',30);
SELECT COUNT(*) FROM Application a JOIN ApplicationResume r USING(application_id) JOIN Interview i USING(application_id) JOIN Offer o USING(application_id) WHERE a.application_id=@app;
ROLLBACK;""",'1')
ok('rollback restores six applications','SELECT COUNT(*) FROM Application','6')
print('ALL DATABASE CHECKS PASSED; retained database for inspection:',db)
