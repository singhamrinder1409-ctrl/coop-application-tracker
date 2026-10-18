# Sprint 1 rubric and feedback audit

Audit date: 2026-10-18. Basis: both user-supplied rubric/feedback PDFs, the pasted Sprint 1 instructions, every prior commitment in `docs/archive/KICKOFF_SPRINT_PLAN.md`, and all nine PDFs in the Desktop `csc 370` folder. Course objectives and slide references are mapped in `docs/COURSE_ALIGNMENT.md`. This audits the submission evidence; it does not promise a grade or claim that a video/public submission already exists.

## 1. Delivery: evidence of achievement (100 points)

| Rubric condition | Check performed | Result / evidence |
| --- | --- | --- |
| Clearly recap every goal from the prior plan | Compared all six numbered next-sprint goals and six success criteria with the current delivery matrix | Covered in `SPRINT_PLAN.md`: written TA feedback, constraint improvements, algebra rules, inheritance/weak-entity decisions, data, more reports and workflow |
| Include goals set by the teaching team | Split every written feedback issue into the nine checks below | All have concrete artefacts and checks; no comment silently omitted |
| Show evidence for achievement, not assertions alone | Loaded schema and data in actual MySQL; compared every report with independently specified rows; rejected invalid writes; executed workflow and rollback | 55 passing database checks in `evidence/mysql-verification.txt`; seven report results in `evidence/demo-output.tsv` |
| Evidence withstands independent testing | Verifiers are committed, use no Python dependencies, accept configured MySQL connection, and use fresh random schemas | README commands; design, worked-example and migration verifiers; a clean tracked-file export was verified before final commit |
| Contrast previous sprint and current progress | Compared archived eight-table DDL and five reports with new design | Resume selection decomposed/enforced; nine tables; seven reports; complete diagrams; full theory and migration preserving original assignments |
| Demonstrate in the video | Timed script maps show/say actions to artefacts | Script ready; actual recording still required |

## 2. Delivery: justification for missed goals (100 points)

| Rubric condition | Check performed | Result / evidence |
| --- | --- | --- |
| Account for all original and TA-set goals | Reconciled archived plan, feedback and delivery table | No known unimplemented technical goal remains against those supplied materials |
| Explain genuinely missed goals accurately | Rechecked the previously asserted live-TA-review requirement | Corrected: the plan requires a review, not a live meeting. The written TA review was supplied and incorporated. No new interview or approval is claimed |
| Explain technical blockers precisely rather than inventing excuses | Reviewed known limitations | Domain FD/MVD assumptions, MySQL DDL implicit commits and migration prerequisites are documented; no fabricated deadline, client interview or performance claim |
| Keep delivery claims consistent with evidence | Separated implementation from submission | Video, remote publication/access and Brightspace submission remain open; these must not be presented as completed |
| Adjust next-sprint scope to realistic velocity | Checked task-hour total and dependencies | 21 person-hours plus 3-hour buffer, explicitly an estimate rather than measured velocity; optional CTE/window work is cut first if capacity is insufficient |

## 3. Planning: improvement against course-level competencies (100 points)

| Rubric condition | Check performed | Result / evidence |
| --- | --- | --- |
| Name course-level competencies explicitly | Read Welcome lecture slides 6-8 | Actual names now used: Data Analytics, Data Modelling, Back-end Engineering |
| Demonstrate a current limitation with respect to each | Inspected schema, queries, diagrams and client files | Basic reports without chart/scaled timings; evolving domain assumptions; no client API or restricted-account integration |
| Describe measurable development from that limitation | Checked every S2 goal has an objective test and evidence | Advanced expected-row reports/chart/timings; model regression; transactional parameterized client and allowed/denied access checks |
| Show examples of how achievement will be measured | Checked examples are concrete, not “improve SQL” | Exact fixture rows, 1,000-application timing fixture, chart/SQL equality, rollback on induced failure, forbidden operation denied |
| Keep scope coherent and accountable | Checked proposed owners, effort, prerequisites and scope-cut rule | Sprint 2 matrix; role/API work follows schema/report regression; optional extensions have lower priority |

## 4. Planning: coverage of new module competencies (100 points)

| Rubric condition | Check performed | Result / evidence |
| --- | --- | --- |
| Cover current sprint through Advanced Relational Design | Reconciled supplied lecture goals and advanced topics explicitly named in feedback | Complete conceptual/relational design, multiplicities, FDs/closures/keys/BCNF, algebra constraints, weak entities/inheritance, minimal bases, projection, 3NF and 4NF |
| Plan next sprint through Advanced SQL | Checked coverage matrix and acceptance criteria | Joins, aggregation/HAVING, NULL/bag semantics, correlated/nested queries, EXISTS/NOT EXISTS, set operations, views and transactional SQL/client operations |
| Give objective end-of-sprint evaluation examples | Checked S2-1 through S2-6 | Every goal names outputs, fixture or failure cases, and pass conditions |
| Avoid claiming unseen official requirements | Inventoried Desktop materials | Only lectures 01-09 were supplied. Separate advanced-module decks were absent; CTE/window work is labelled a proposed extension. Scope mapping uses the assignment and explicit feedback rather than invented official wording |

## Every specific feedback item

The feedback contains four criterion comments. Their individual concerns expand to the following nine checks:

| ID | Feedback concern | Correction / exact evidence | Audit status |
| --- | --- | --- | --- |
| F1 | BCNF was not checked per table | `NORMALIZATION.md` lists the FD model, minimal basis and all candidate keys for each of nine tables; `scripts/design.py` checks closures, minimality and all non-key determinants | Addressed |
| F2 | ERD omitted most attributes, including JobPosting details | `CONCEPTUAL_ERD.svg` follows lecture Chen notation; 50 descriptive attributes/identifiers plus relationship mapping account for every one of the 59 SQL columns; complete `ERD.svg` and generated schema show all 13 JobPosting columns | Addressed; both diagrams visually checked |
| F3 | A course-level competency was not named | Sprint 2 matrix and `docs/COURSE_ALIGNMENT.md` use the three actual names from the Welcome slides | Addressed |
| F4 | Current project limitation was not stated against competency | Each course-level row has a specific current-limit column and an objective change/test | Addressed |
| F5 | FDs in ERDs omitted | `NORMALIZATION.md`: identifier and multiplicity-derived FDs, including posting_id -> employer_id and the non-reversible resume relationship | Addressed |
| F6 | Minimal bases omitted | Singleton-RHS basis for each production table; worked redundant-FD removal; exhaustive closure-equivalence and minimality checks in `verify_theory.py` | Addressed |
| F7 | Projecting FDs omitted | Worked Flat-to-(A,N,P) example derives A->N through removed S; projected basis compared on every subset | Addressed |
| F8 | 3NF omitted | Allocation example checks both keys, prime attributes, BCNF violation and lost local dependency enforcement after lossless decomposition | Addressed |
| F9 | 4NF omitted | Independent skills/cities MVD, explicit four-row lossless reconstruction and missing-combination counterexample; production MVD assumptions stated separately | Addressed; no claim that an FD test proves arbitrary MVDs |

## Every remaining assignment/delivery requirement

| Requirement | Status and action |
| --- | --- |
| Continue the previous MySQL-backed system | Done. Same Co-op Application Tracker; Desktop baseline matches all original tracked files byte for byte. Research checkout is the updated working copy |
| Prove completion against prior success criteria | Done in delivery matrix and executable evidence, including two genuinely new reports |
| Plan through Advanced SQL | Done with named competencies, current limitations, acceptance criteria, effort and proposed owners |
| Cite online ideas/code used | SOURCES.md cites MySQL references and course sources; code/examples were authored for this project, and Codex assistance is disclosed |
| Full-team consent for AI use | **Group action remaining.** Welcome lecture slide 15 requires full-team consent and responsible use; consent from every member has not been verified |
| Repository URL and exact commit hash | Local Git commit will contain this audit and evidence. **Remote URL/push remain:** no remote is configured. Use final `git rev-parse HEAD`, not a superseded hash |
| Instructor and TA-client access if private | **Group action remaining:** verify after selecting/publishing the repository |
| Recorded progress/planning video | **Group action remaining:** record `TEAM_VIDEO_SCRIPT.md` with actual evidence; a script is not a video |
| Video duration | Formula gives 11 minutes for three members; pasted example says 8. Target 7:30 and keep the measured export below 8:00 to satisfy both. Runtime is not yet measured |
| One group member submits in Brightspace | **Group action remaining:** submit the repository URL/hash and video; verify group enrolment if submission fails |

## Corrections made during this audit

1. Added two new reports: workload including zero-application students, and missing resume selections. Baseline had five; current pack has seven.
2. Replaced execution-only report testing with independent expected-row comparisons against the report SQL itself, preserving duplicate multiplicities.
3. Corrected the ownership constraint to use explicit theta joins; a natural join could hide ownership violations by equating student_id.
4. Strengthened diagram verification to compare attributes within each entity and FK relationships, rather than substring matches across a whole file.
5. Added separately executable minimal-basis/projection/3NF/4NF worked-example checks.
6. Removed the unsupported requirement for a live TA meeting; documented the supplied written review and no new approval claim.
7. Restored lecture-style Chen conceptual notation alongside the complete relational diagram.
8. Used actual course competency names and added the missing planned analytics visualization/timing and restricted-client/API evidence.
9. Added and tested an ALTER-based migration from the populated kick-off fixture; corrected MySQL's INSERT-SELECT/trigger interaction before the successful run.
10. Added the course's actual full-team AI-consent requirement to the submission checklist.

The repository-side work has evidence for each supplied rubric/feedback requirement. Final grading still depends on the team's explanation and the actual submitted video/repository. The open submission actions above cannot be replaced with checked boxes or unsupported claims.
