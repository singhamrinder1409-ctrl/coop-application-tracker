# Audit after the course folder was expanded

Reviewed on 2026-10-18. The folder now contains 34 source files: 14 lecture PDFs, one practice-exam PDF, 16 transcripts and three worksheet archives. The original nine PDF fingerprints are unchanged. Fingerprints and the review method are in MATERIALS_REVIEW.md. The work extends the kick-off tracker.

## Added material and resulting changes

| Added source | Required method / clarification | Project action and evidence |
| --- | --- | --- |
| CSC370-10 Improving Conceptual Designs | Assess eight quality criteria and classify information-preserving/changing transformations | Added CONCEPTUAL_DESIGN_REVIEW.md. It maps all eight criteria to actual tracker choices, including the conditionally redundant student/application/resume cycle and the limits of migration preservation |
| CSC370-11 ERDs to FDs | Derive identifier and relationship FDs; verify relations and normality rather than blindly translating shapes | Expanded the conceptual review's entity/link FD verification and matched multiplicities to production keys. Existing exact entity/attribute/FK tests remain applicable |
| CSC370-12 Projecting FDs | Compare all subset closures, produce a minimal basis and project inferred dependencies | Added a complete eight-row projection closure table to NORMALIZATION.md; every restricted closure is checked by verify_theory.py |
| CSC370-23 3NF - corrected | Execute the full synthesis algorithm, including adding a key relation when no FD-generated relation contains a superkey | Added FlatApplicationNotes synthesis into AS, AP, SN, QT plus the necessary AQ relation. Tests check candidate key, projected 3NF, dependency preservation and exact reconstruction |
| CSC370-24 4NF & MVDs | Apply the formal tuple-swap definition, identify trivial/nontrivial MVDs and decompose losslessly | Added the definition, triviality/complementarity, FD-as-MVD reasoning and a counterexample to applying FD splitting to MVDs; tests directly check tuple swapping and decomposition |
| Projecting Functional Dependencies worksheet | Show closure computation and minimal-basis reasoning, not just delete FDs mentioning removed columns | Applied to the tracker-shaped Flat example with an independently checked full projection table |
| Third Normal Form worksheet | Synthesis/key augmentation; recognize that BCNF implies 3NF | Full synthesis demonstration added; no unnecessary change to already-BCNF production tables. Explicitly notes why a “BCNF but not 3NF” example cannot exist |
| Keys, ERDs & SQL DDL worksheet, including six packaged figures | Distinguish entity identifiers, relationship keys and FK placement; understand composite and many-to-one cases | Checked the existing schema and the conceptual/relational mapping against that method. Worksheet example domains are not extra application requirements |
| Introductory transcript (misnamed CSC 485A_586F) | Data Analytics progresses from correct SQL to analytical queries; visualization is outside course scope. Back-end foundations are transactions/ACID; an API is aspirational | Core next-sprint goals are correct result sets, views and documented transaction behavior. Charts, APIs, access-role integration and scaled performance experiments are optional |
| Remaining 15 transcripts | Explain basic SQL, multiplicities, FDs/keys, BCNF, constraints, inheritance, quality, ERD/FD links, projection, 3NF and 4NF | Indexed all text and reviewed relevant project/competency/policy and advanced-design passages. Reconciled with the slides, archived goals and rubric. No historical relative deadline is used as a current submission date |

The added ten-page practice exam emphasizes explaining changes to multiplicities, identifiers and constraints, and comparing designs with the course criteria. These are included as preparation prompts in TEAM_REVIEW_GUIDE.md; they add no production features or separate project submission.

## Scope and interpretation

The corrected 3NF deck and closures identify both city/title and theatre/title as cinema keys. NORMALIZATION.md explains the inconsistent review sentence in the 4NF deck and verifies the result.

The production schema remains nine tables with seven reports. The extra normalization relations are labelled design experiments. The core plan covers the named Advanced SQL operations; CTE/window analysis, charts and APIs are optional. A separate Advanced SQL deck was not supplied.

## Final evidence

- 56 MySQL database checks: schema/columns, all report result sets, valid workflow/rollback and invalid-write rejections.
- 15 migration checks: upgrade the exact kick-off fixture, preserve all original application/resume associations and reject invalid legacy ownership before table changes.
- Nine production-relation key/minimal-basis/BCNF checks and exact diagram coverage.
- 12 worked theory checks, now including full 3NF synthesis/key augmentation and formal MVD properties.
- Chen conceptual diagram: eight entity sets, 50 descriptive attributes/identifiers and relationship mapping of all nine SQL FK columns; complete relational companion accounts for all 59 columns.
- Ten CLI safety checks reject optimized modes that would disable assertions.
- Five verification commands run from a clean project export; actual outputs saved in evidence/.

RUBRIC_AUDIT.md remains the criterion-by-criterion decision record. The remaining human submission actions remain full-team consent/review, recording and measuring the actual video, selecting/publishing a repository with access, and submitting its URL, exact final hash and video. Publication and recording are recorded separately from technical verification.
