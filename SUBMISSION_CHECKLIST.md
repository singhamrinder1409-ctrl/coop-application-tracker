# Sprint 1 submission checklist

## Completed in this repository

- [x] All four rubric criteria and every specific feedback issue audited in RUBRIC_AUDIT.md.
- [x] Five verification commands passed from a clean project export, without repository-local dependencies.

- [x] Every kick-off commitment recapped with status and evidence in SPRINT_PLAN.md.
- [x] All four written feedback gaps addressed, including Advanced Relational Design topics.
- [x] Course-style Chen conceptual ERD and complete relational diagram/schema, with all 59 SQL columns accounted for.
- [x] Expanded material set reviewed (14 PDFs, 16 transcripts, three worksheets); actual course-level competency names and transcript scope clarifications used.
- [x] Upgrade from the original kick-off schema tested without losing original assignments.
- [x] Table-by-table FD, key, minimal basis and BCNF checks; worked projection, 3NF and 4NF explanations.
- [x] Resume ownership enforcement and more than five formal integrity rules.
- [x] Synthetic normal/edge data, seven reporting queries with expected-row assertions and actual MySQL execution evidence.
- [x] Workflow and rejected-write verification; next sprint plan through proposed Advanced SQL scope.
- [x] Full 3NF synthesis/key-relation, formal MVD rules and all eight conceptual-design quality criteria covered with evidence.
- [x] Charts/APIs are optional extensions, consistent with the introductory transcript.
- [x] Team recording script and sources provided.

## Must be completed by the group before Brightspace submission

- [x] Requirements basis confirmed by the group: no separate competency list or additional TA-client requirements; use the supplied assignment and feedback.
- [x] Respond to the supplied written TA review; no live meeting is required or claimed. Design assumptions and absence of new approval are disclosed.
- [ ] Confirm full-team consent for AI assistance (Welcome lecture, slide 15); assistance is disclosed in SOURCES.md.
- [ ] Review code/theory and practice explaining it using docs/TEAM_REVIEW_GUIDE.md; do not claim unperformed work.
- [ ] Record the actual team video. Target 7:30 including transitions and below 8:00 to satisfy both the formula and inconsistent example in the pasted instructions.
- [ ] Measure the exported recording's length; do not rely on the script's estimate.
- [ ] Create or select a GitHub/UVic GitLab remote. None is configured locally.
- [ ] Push the submission commit to the chosen remote and verify the URL resolves to that commit.
- [ ] For a private repository, grant instructor and TA-client access.
- [ ] Include repository URL, exact full commit hash, and video in Brightspace; only one member submits for Group 3.

After the final edit, commit and inspect:

```sh
git status --short
git add .
git commit -m "Complete CSC 370 Sprint 1 evidence and Advanced SQL plan"
git rev-parse HEAD
git remote -v
```

Run these commands inside this project's own Git repository, not the surrounding research repository. If this session already created the final commit, use `git rev-parse HEAD`; do not make an empty replacement commit. Add a remote and push only after selecting the intended account/repository.
