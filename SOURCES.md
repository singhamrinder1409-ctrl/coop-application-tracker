# Sources and assistance

## Assignment and baseline

- `Feedback for Project Kick-Off - Fall 2026 CSC 370 A01 A02 X - University of Victoria.pdf`: feedback on BCNF evidence, ERD completeness, competency/current-limitation planning and Advanced Relational Design coverage.
- `Project Sprint 1 - Fall 2026 CSC 370 A01 A02 X - University of Victoria.pdf`: the four grading criteria.
- Sprint 1 assignment text supplied with this project: current scope through Advanced Relational Design, next scope through Advanced SQL, repository URL/hash and video requirements.
- Original kickoff plan, schema and data: preserved in `docs/archive/`.

## Course material

Sean Chester's supplied CSC 370 materials include 14 lecture PDFs, one practice-exam PDF, 16 transcripts and three worksheet archives. `docs/COURSE_ALIGNMENT.md` connects the course topics to the project.

| PDF | Use in this submission |
| --- | --- |
| CSC370-01_ Welcome!-1.pdf | Competency names, slides 6-8 |
| CSC370-02_ Storing Data w_ SQL-1.pdf | CREATE/ALTER TABLE, scalar types and inserting data |
| CSC370-03_ SQL DQL-2.pdf | Retrieval, projection, selection, renaming, joins and set operations |
| CSC370-4 Conceptual Design .pdf | Chen notation, identifiers, attributes, relationships and roles |
| CSC370-05 Multiplicity.pdf | Participation, relationship keys and relational mapping |
| CSC370-06 FD's & Keys.pdf | Domain FDs, closures, keys and superkeys |
| CSC370-07 BCNF Decomposition.pdf | Violating FDs, decomposition and lossless joins |
| CSC370-08_ Constraints in Relational Algebra.pdf | Empty-result/subset constraints, self-joins and referential integrity |
| CSC370-09_ Inheritance.pdf | Subtype and weak-entity alternatives |
| CSC370-10_ Improving Conceptual Designs.pdf | Eight design-quality criteria and transformation classification |
| CSC370-11_ ERDs to FDs_.pdf | Checking identifier/link FDs and conceptual normality |
| CSC370-12_ Projecting FD's.pdf | FD-set equivalence, minimal bases and projection |
| CSC370-23_ 3NF - corrected.pdf | Prime attributes, preservation tradeoffs and synthesis with key augmentation |
| CSC370-24_ 4NF & MVD's.pdf | Tuple-swap definition, MVD properties and 4NF decomposition |

The three worksheets provide practice in ERD keys/DDL, projecting FDs and 3NF synthesis. Their methods are applied to project-shaped examples. The file named `CSC 485A_586F Lectur-transcript.txt` identifies CSC 370 in its opening; it supplies the introductory guidance that visualization is outside scope and APIs are aspirational. Other transcripts support the corresponding lessons. Relative dates in transcripts are not used to set this submission's deadline.

The corrected 3NF deck and closure calculations identify both {city,title} and {theatre,title} as cinema keys. The 4NF review slide 7 gives an inconsistent key statement; the corrected 3NF material and closure calculations support both keys. Course files are referenced without redistributing the supplied PDFs or transcripts.

The ten-page `Fall 2026 CSC 370 A01 A02 X - Data Modelling Practice Exam (1 booklet).pdf` supplies rehearsal formats: explain changed constraints with counterexamples, derive ERD FDs, adjust keys/DDL, and justify design alternatives (questions 16-21). Its movie/ticket examples are not tracker requirements.

## MySQL documentation

- [CREATE TABLE](https://dev.mysql.com/doc/refman/8.4/en/create-table.html): table constraints and explicit storage-engine selection.
- [Trigger syntax and examples](https://dev.mysql.com/doc/refman/8.4/en/trigger-syntax.html): trigger bodies and OLD/NEW references.
- [Stored routines and privileges](https://dev.mysql.com/doc/refman/8.4/en/stored-routines-privileges.html): CREATE ROUTINE, ALTER ROUTINE and EXECUTE permissions.

The changes use the course methods and MySQL interfaces listed above.

## Assistance and review

OpenAI Codex assisted with the SQL changes, verification scripts, diagrams, theory examples and draft documentation.
