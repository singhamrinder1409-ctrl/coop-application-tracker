#!/usr/bin/env python3
"""Exercise the archived kickoff-to-Sprint-1 upgrade on isolated fresh schemas."""
import os, re, subprocess, uuid
from pathlib import Path
root=Path(__file__).resolve().parents[1]
args=[os.environ.get('MYSQL_BIN','mysql'),'--batch','--raw','--skip-column-names','-u',os.environ.get('MYSQL_USER','root')]
if os.environ.get('MYSQL_SOCKET'): args+=['--socket='+os.environ['MYSQL_SOCKET']]
db='coop_sprint1_migration_'+uuid.uuid4().hex[:12]
def sql(source): return subprocess.run(args,input=source,text=True,capture_output=True)
def run(label,source,expected=None):
    r=sql(source)
    assert r.returncode==0,(label,r.stderr)
    if expected is not None: assert r.stdout.strip()==expected,(label,r.stdout,expected)
    print('PASS',label)
# Never execute the historical DROP DATABASE: only initialize a fresh random schema.
old=(root/'docs/archive/KICKOFF_SCHEMA.sql').read_text()
old=re.sub(r'DROP DATABASE IF EXISTS coop_application_tracker;\s*','',old)
old=old.replace('coop_application_tracker',db)
seed=(root/'docs/archive/KICKOFF_SEED.sql').read_text().replace('coop_application_tracker',db)
run('archived kick-off schema and data load',old+'\n'+seed)
run('capture original references','USE '+db+'; SELECT GROUP_CONCAT(CONCAT(application_id,\':\',resume_id) ORDER BY application_id) FROM Application;','1:1,2:2,3:3,4:4')
run('construct invalid legacy ownership','USE '+db+'; UPDATE Application SET resume_id=3 WHERE application_id=1;')
migration=(root/'migrations/001_sprint1.sql').read_text().replace('coop_application_tracker',db)
r=sql(migration)
assert r.returncode!=0 and 'ERROR 1644' in r.stderr and 'cross-student resume' in r.stderr,r.stderr
print('PASS preflight rejects invalid legacy ownership')
run('rejected preflight preserves old application column','USE '+db+"; SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='Application' AND column_name='resume_id';",'1')
run('rejected preflight creates no assignment table','USE '+db+"; SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='ApplicationResume';",'0')
run('restore legacy ownership','USE '+db+'; UPDATE Application SET resume_id=1 WHERE application_id=1;')
run('migration executes without database reset',migration)
run('all legacy resume associations retained','USE '+db+"; SELECT GROUP_CONCAT(CONCAT(application_id,':',resume_id) ORDER BY application_id) FROM ApplicationResume;",'1:1,2:2,3:3,4:4')
run('old resume column removed','USE '+db+"; SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='Application' AND column_name='resume_id';",'0')
run('legacy application and student rows retained','USE '+db+'; SELECT (SELECT COUNT(*) FROM Application),(SELECT COUNT(*) FROM Student);','4\t3')
r=sql('USE '+db+'; UPDATE ApplicationResume SET resume_id=3 WHERE application_id=1;')
assert r.returncode!=0 and 'ERROR 1644' in r.stderr,r.stderr
print('PASS upgraded schema enforces resume ownership')
run('four ownership triggers installed','USE '+db+"; SELECT COUNT(*) FROM information_schema.triggers WHERE trigger_schema=DATABASE();",'4')
print('ALL MIGRATION CHECKS PASSED; retained disposable database:',db)
