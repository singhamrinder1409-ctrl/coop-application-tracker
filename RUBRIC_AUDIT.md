# Sprint 1 rubric and feedback audit

Reviewed against the two supplied rubric/feedback PDFs, the pasted assignment, the archived kick-off plan and the course sources listed in SOURCES.md. Execution results are in evidence/. Recording, publication and Brightspace submission remain group actions.

## Four grading criteria

| Criterion (100 points each) | Required evidence | Current coverage |
| --- | --- | --- |
| Delivery: achievement of sprint goals | Recap every prior and TA-set goal, show progress from the baseline and provide independently testable evidence | SPRINT_PLAN.md maps the six prior objectives and their success criteria. The database, report, migration, diagram and theory checks have saved results. TEAM_VIDEO_SCRIPT.md identifies what to show in the recording |
| Delivery: justification for missed goals | Account for each goal and explain any miss with concrete evidence and its effect | The implementation evidence covers the supplied technical commitments. Written TA feedback is incorporated; no subsequent meeting or approval is recorded. Video, publication/access and upload remain pending. The report states FD/MVD assumptions and migration limits |
| Planning: course-level improvement | Name the competency, identify the current limitation and set measurable improvement criteria | The plan uses Data Analytics, Data Modelling and Back-end Engineering, with current limitations, proposed owners, effort and checks for each. Core effort totals 18 person-hours; optional work has a separate allowance |
| Planning: new module coverage | Cover the current scope through Advanced Relational Design and plan through Advanced SQL, with objective end-of-sprint checks | Course mapping covers conceptual quality, FDs/keys/BCNF, algebra constraints, weak entities/inheritance, minimal bases/projection, 3NF and 4NF. Next-sprint checks cover joins, aggregation/HAVING, nested queries, EXISTS, set operations, views and SQL transactions |

## Individual feedback concerns

| Concern | Evidence addressing it |
| --- | --- |
| BCNF was not checked per table | NORMALIZATION.md defines the FD basis and candidate keys for all nine tables. scripts/design.py checks minimality, closures and non-key determinants under that model |
| ERD attributes were missing | CONCEPTUAL_ERD.md maps 50 descriptive attributes/identifiers and nine SQL FK columns through relationships. ERD.svg and RELATIONAL_SCHEMA.md show all 59 columns, including all 13 JobPosting columns |
| Course-level competency was unnamed | SPRINT_PLAN.md and docs/COURSE_ALIGNMENT.md use the three names from Welcome slides 6-8 |
| Current limitation was unspecified | Each core next-sprint goal identifies a present limitation and a measurable result |
| FDs in ERDs were omitted | NORMALIZATION.md and docs/CONCEPTUAL_DESIGN_REVIEW.md derive identifier/link FDs and check them against multiplicities |
| Minimal bases were omitted | Production bases and a worked reduction are documented; deletion and closure-equivalence checks are executable |
| FD projection was omitted | The Flat example has a complete subset-closure table; tests compare the projected basis with every restricted closure |
| 3NF was omitted | Allocation explains the BCNF/preservation tradeoff. Full synthesis creates AS, AP, SN, QT and the required AQ key relation, with preservation and reconstruction checks |
| 4NF was omitted | The tuple-swap definition, triviality/complementarity, non-splitting counterexample and lossless independent-value decomposition are documented and tested. Production MVD assumptions are stated separately |

## Scope and source checks

The current project extends the original Co-op Application Tracker. The Desktop kick-off copy matches the archived baseline; a migration preserves its four original application/resume assignments. The Desktop source files and existing user databases were unchanged.

The material review covers 15 PDFs (14 lecture decks and one practice exam), 16 transcripts and three worksheet archives. Corrected 3NF slides and computed closures resolve an inconsistent key statement in the 4NF review. The introductory transcript places visualization outside course scope and an API at an aspirational stage; charts, APIs and CTE/window work remain optional. A separate Advanced SQL deck was not supplied, so the plan names its SQL operations without asserting an unseen official lesson list.

SOURCES.md records course references, MySQL documentation and Codex assistance. The group must confirm full-team consent and understand the submitted work. The verifiers establish their listed results, not stakeholder approval or coverage of unspecified requirements.

## Submission actions still open

Publish the repository and verify instructor/TA access, record and measure the video, then have one group member submit its URL, final commit hash and video. Use SUBMISSION_CHECKLIST.md. The 7:30 recording target stays below the pasted example's eight-minute limit and the formula's eleven-minute limit for three members.
