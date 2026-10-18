# Sources Used

The project idea and database design were based on the CSC 370 kick-off instructions, rubric, and lecture slides provided for the course.

## Course Instructions

- `Project Kick-Off - Fall 2026 CSC 370 A01 A02 X - University of Victoria.pdf`
- Brightspace kick-off instructions pasted by the group

## Lecture Slides Used

- `CSC370-01_ Welcome!-1.pdf`
- `CSC370-02_ Storing Data w_ SQL-1.pdf`
- `CSC370-03_ SQL DQL-2.pdf`
- `CSC370-4 Conceptual Design .pdf`
- `CSC370-05 Multiplicity.pdf`
- `CSC370-06 FD's & Keys.pdf`
- `CSC370-07 BCNF Decomposition.pdf`
- `CSC370-08_ Constraints in Relational Algebra.pdf`
- `CSC370-09_ Inheritance.pdf`

## Main Course Ideas Used

- SQL DDL and `CREATE TABLE`
- relational databases as tables with tuples and attributes
- conceptual design and ERDs
- entity sets, attributes, identifiers, and relationships
- relationship multiplicity
- functional dependencies
- keys and superkeys
- BCNF and decomposition
- foreign keys and referential integrity
- constraints in relational algebra
- inheritance and weak entity sets as possible future design ideas

## External Sources

No external code sources were used for the SQL files in this kick-off stage.

## Sprint 1 sources and provenance (2026-10-18)

- User-supplied `Feedback for Project Kick-Off - Fall 2026 CSC 370 A01 A02 X - University of Victoria.pdf`: specific feedback on BCNF, ERD completeness, current limitations/course competencies, minimal bases, projecting FDs, 3NF and 4NF.
- User-supplied `Project Sprint 1 - Fall 2026 CSC 370 A01 A02 X - University of Victoria.pdf`: four-criterion grading rubric (delivery evidence, missed goals, course-level planning and module-level planning).
- Assignment text pasted by the user: scope through Advanced Relational Design now, planning through Advanced SQL next, git URL/hash and video requirements.
- Existing kick-off commit `ac978f8`: actual baseline plan and schema. The original slide list above was inherited from kick-off. All nine actual PDFs were subsequently found and read in the Desktop course folder; see the verified inventory below. There is no separate competency list or additional TA requirement beyond the supplied materials.
- [MySQL 8.4 CREATE TABLE reference](https://dev.mysql.com/doc/refman/8.4/en/create-table.html): key, foreign key and check syntax.
- [MySQL trigger syntax and examples](https://dev.mysql.com/doc/refman/8.4/en/trigger-syntax.html): trigger structure and OLD/NEW access. Code was written for this project, not copied from an external implementation.

The Sprint 1 implementation, test scripts, theory examples, diagram generator and draft report/script were prepared with OpenAI Codex assistance. The group must review them, understand the reasoning, and accurately represent contributions under applicable course policy. Test evidence records actual MySQL 8.4.8 and Python runs; it does not establish that a TA interview, video recording, or publication occurred.

## Desktop course materials verified during the rubric audit

Directory: `/Users/ammy/Desktop/csc 370`. Exact filenames, page counts and SHA-256 digests are recorded in `docs/MATERIALS_REVIEW.md`. All nine decks were reviewed, not merely listed:

- `CSC370-01_ Welcome!-1.pdf`
- `CSC370-02_ Storing Data w_ SQL-1.pdf`
- `CSC370-03_ SQL DQL-2.pdf`
- `CSC370-05 Multiplicity.pdf`
- `CSC370-06 FD's & Keys.pdf`
- `CSC370-07 BCNF Decomposition.pdf`
- `CSC370-08_ Constraints in Relational Algebra.pdf`
- `CSC370-09_ Inheritance.pdf`
- `CSC370-4 Conceptual Design .pdf`

Welcome slides 6-8 supply the actual competency names and descriptions. Slide 15 states the full-team-consent/responsible-use condition for generative AI. Conceptual Design slides 9-10 specify the class's Chen-style notation; the new conceptual diagram follows it. Lecture 08 guides the empty-result, self-join and subset constraint forms. Lecture 09 guides the subtype/weak-entity alternatives. The advanced topics absent from the folder are included because the written feedback explicitly requires them; we do not falsely attribute them to a missing deck.

These are privately supplied course references. The repository records their names and relevant slide numbers without redistributing lecture PDFs. `RUBRIC_AUDIT.md` and `docs/COURSE_ALIGNMENT.md` map each source requirement to project evidence.
