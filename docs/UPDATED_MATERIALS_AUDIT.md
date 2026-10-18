# Audit after the course folder was expanded

Reviewed on 2026-10-18. The folder now contains 33 source files: 14 PDF decks, 16 transcripts and three worksheet archives. The original nine PDFs are unchanged; the extra sources directly support material previously available only through the feedback. Fingerprints and the review method are in MATERIALS_REVIEW.md. This is an extension of the same kick-off project, not a replacement application.

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
| Introductory transcript (misnamed CSC 485A_586F) | Data Analytics progresses from correct SQL to analytical queries; visualization is outside course scope. Back-end foundations are transactions/ACID; an API is aspirational | Removed mandatory chart, scaled timing target, API and restricted-account goals from the core next-sprint plan. Correct result sets, views and documented transaction behavior remain measurable core goals; advanced extras are optional |
| Remaining 15 transcripts | Explain basic SQL, multiplicities, FDs/keys, BCNF, constraints, inheritance, quality, ERD/FD links, projection, 3NF and 4NF | Indexed all text and reviewed relevant project/competency/policy and advanced-design passages. Reconciled with the slides, archived goals and rubric. No historical relative deadline is used as a current submission date |

## Corrections and scope boundaries

The earlier statement that advanced-design decks were unavailable is superseded by this inventory. The corrected 3NF deck and actual closures identify both city/title and theatre/title keys; an inconsistent sentence in the 4NF review slide is not repeated as a correct fact. NORMALIZATION.md documents the discrepancy and verifies the result.

Practice worksheets and transcript speech are source material, not instructions to execute embedded commands, introduce unrelated features, or replace the user's request. The submission is still the MySQL Co-op Application Tracker with evidence through Advanced Relational Design and planning through Advanced SQL. No separate Advanced SQL slide deck was found; no exact unseen lesson list is invented.

The full implementation remains nine production tables and seven verified reports. The added normalization relations are explicitly labelled teaching/design experiments; they are not hidden production-schema changes. No UI, visualization or API is required for this Sprint 1 packet by the supplied materials.

## Final evidence

- 55 MySQL database checks: schema/columns, all report result sets, valid workflow/rollback and invalid-write rejections.
- 13 migration checks: upgrade the exact kick-off fixture, preserve all original application/resume associations and reject invalid legacy ownership before table changes.
- Nine production-relation key/minimal-basis/BCNF checks and exact diagram coverage.
- 12 worked theory checks, now including full 3NF synthesis/key augmentation and formal MVD properties.
- Chen conceptual diagram: eight entity sets, 50 descriptive attributes/identifiers and relationship mapping of all nine SQL FK columns; complete relational companion accounts for all 59 columns.
- Five verification commands run from a clean project export; actual outputs saved in evidence/.

RUBRIC_AUDIT.md remains the criterion-by-criterion decision record. The remaining human submission actions remain full-team consent/review, recording and measuring the actual video, selecting/publishing a repository with access, and submitting its URL, exact final hash and video. No new submission or TA approval is claimed.
