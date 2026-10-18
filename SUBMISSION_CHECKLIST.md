# Sprint 1 submission checklist

## Completed in this repository

- [x] Every kick-off commitment recapped with status and evidence in SPRINT_PLAN.md.
- [x] All four written feedback gaps addressed, including Advanced Relational Design topics.
- [x] Complete ERD and generated relational schema.
- [x] Table-by-table FD, key, minimal basis and BCNF checks; worked projection, 3NF and 4NF explanations.
- [x] Resume ownership enforcement and more than five formal integrity rules.
- [x] Synthetic normal/edge data, five reporting queries and actual MySQL execution evidence.
- [x] Workflow and rejected-write verification; next sprint plan through proposed Advanced SQL scope.
- [x] Team recording script and sources provided.

## Must be completed by the group before Brightspace submission

- [x] Requirements basis confirmed by the group: no separate competency list or additional TA-client requirements; use the supplied assignment and feedback.
- [ ] Confirm TA-client assumptions or explicitly disclose review still pending.
- [ ] Review code/theory and practice explaining it; do not claim unperformed work.
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
