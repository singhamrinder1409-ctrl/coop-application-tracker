# Course material alignment

Reviewed all nine PDFs in `/Users/ammy/Desktop/csc 370`. The full inventory is in `SOURCES.md`. The folder contains lectures 01-09; it does not contain a separate Advanced Relational Design or Advanced SQL slide deck. The supplied assignment and feedback still explicitly require those topic areas, so their worked examples and future plan are included rather than omitted. This document distinguishes lecture-supported requirements from proposed extensions.

## Actual course-level competency names

`CSC370-01_ Welcome!-1.pdf`, slides 6-8, names **Data Analytics**, **Data Modelling**, and **Back-end Engineering**. These are the names used in the revised sprint plan, rather than invented competency labels.

| Competency | Meaning in the supplied lecture, paraphrased | Current project limitation | Measurable next-sprint improvement |
| --- | --- | --- | --- |
| Data Analytics | Use expressive SQL to derive insights and communicate them through coherent visualizations within practical execution time | Seven verified basic reports; no complex report pack, visualization or scaled timing evidence | S2-1 adds 8 advanced reports and one chart whose values match the SQL result; record EXPLAIN and timings on a fixed larger fixture, clearly separating measured results from targets |
| Data Modelling | Turn application requirements into normalized abstractions with clear conceptual/relational schemata and trustworthy populated instances | Current assumptions and synthetic fixture cover one student-facing workflow; future requirements could introduce new FDs/MVDs | S2-5 keeps the Chen diagram, relational model and FD/MVD decisions synchronized; rerun all coverage/key/normalization and migration checks; record fixture provenance and any new requirements |
| Back-end Engineering | Connect applications and databases using compatible API/SQL and appropriate access, consistency and concurrency controls | Database enforcement exists, but there is no client API or tested role-restricted access | S2-3 builds a parameterized client/API operation with transaction success/failure tests and a restricted DB user; test expected allowed/denied operations; explicitly defer a full concurrent workload benchmark |

## Lecture-by-lecture mapping

| Supplied lecture and relevant slides | Lesson objective, paraphrased | Sprint 1 evidence | Next-sprint continuation |
| --- | --- | --- | --- |
| 01 Welcome, 4-8, 15 | Name course goals; responsible team use of generative AI | This matrix uses the actual three competency names; SOURCES.md discloses Codex assistance | Team confirms full-team consent and can explain the project individually |
| 02 Storing Data w/ SQL, 3, 30-36 | Execute CREATE/ALTER statements and insert typed scalar values | schema.sql; current seed; tested `migrations/001_sprint1.sql` uses ALTER TABLE while preserving kick-off data | Clean-load and migration regression after schema changes |
| 03 Retrieving Data with SQL, 3, 9-22 | Retrieve data using simple SQL and relate it to selection/projection/rename/joins/set operations | Seven reports with exact expected rows; constraints use π, σ, ρ, difference and theta joins | S2-1 adds EXISTS, correlated queries, HAVING and set-operation reports, checking bag/NULL semantics |
| 04 Conceptual Design, 4, 6-10, 14-18, 23-28 | Construct a conceptual ERD using entity sets, attributes, identifiers, relationships and roles | CONCEPTUAL_ERD.svg uses the course's Chen-style notation; 50 descriptive attributes/identifiers plus relationships; relational diagram accounts for every SQL column | Regenerate both levels of model after changes |
| 05 Multiplicity, 3, 16-19, 22-32 | Determine binary/multi-way multiplicities and how they affect identifiers and table mapping | CONCEPTUAL_ERD.md maps every relationship and min/max participation; explains the student/posting association and why independent binary relationships suffice | Preserve relationship keys; test altered uniqueness if requirements change |
| 06 FD's & Keys, 4, 29, 34-49, 55-57 | Identify domain FDs, compute closures and determine keys/superkeys | NORMALIZATION.md states assumptions and all keys; exhaustive closure checks for all nine production relations | Re-evaluate keys whenever requirements add dependencies; do not infer FDs from coincidental seed patterns |
| 07 BCNF Decomposition, 4, 20, 24-30, 36-39 | Decompose using violating FDs and reconstruct through lossless joins | Resume-selection decomposition and worked Flat example; verified closure/intersection conditions | Retain dependency-preservation reasoning and exact migration tests |
| 08 Constraints in Relational Algebra, 3, 19-20, 39, 45, 50-58 | Express value, key, FD and referential integrity constraints algebraically | docs/CONSTRAINTS.md includes empty-result/subset rules and renamed self-join constraints; database checks exercise enforcement | Rerun all constraint counterexamples and translate any new cross-table rule carefully |
| 09 Weak Entity Sets & Inheritance, 3, 14-23, 25-27 | Simplify modelling through subsets and borrowed identifiers | Explicit Interview weak-entity alternative and chosen surrogate mapping; considered/rejected unnecessary posting inheritance; subtype PK/FK approach explained | Add a subtype only if distinct attributes or restricted relationships justify it |

## Feedback topics beyond the supplied slide inventory

FDs in ERDs, minimal bases, projected FDs, 3NF and 4NF are each covered in NORMALIZATION.md with production implications and worked examples. `scripts/verify_theory.py` verifies those examples. Advanced SQL is planned through joins, aggregates/HAVING, subqueries/EXISTS, set operations, views, NULL/bag semantics and transactional client operations. CTEs/window functions are explicitly proposed extensions, not claims about an unavailable module's exact contents.

## Exact relational-algebra forms used for key/FD rules

Following lecture 08, rule statements in first-order logic can also be written as empty self-join results. With `a := ρ_a(Application)` and `b := ρ_b(Application)`:

`σ_(a.student_id=b.student_id ∧ a.posting_id=b.posting_id ∧ a.application_id≠b.application_id)(a × b) = ∅`.

This encodes the alternate application key. For Interview, replace the matched fields with application_id/interview_round and require distinct interview_id. For the Student FD student_id -> full_name, rename Student as s and t and require:

`σ_(s.student_id=t.student_id ∧ s.full_name≠t.full_name)(s × t) = ∅`.

The cross-table resume-ownership rule uses explicit theta joins on the reference keys, not a natural join that could discard violations by also joining on student_id. Optional values are discussed separately in NORMALIZATION.md.
