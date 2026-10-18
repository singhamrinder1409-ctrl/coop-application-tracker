# Course material alignment

This maps the supplied course material to Sprint 1 evidence and the next-sprint plan. Current coverage extends through Advanced Relational Design. No separate Advanced SQL deck was supplied; the plan identifies the SQL operations it proposes to demonstrate.

## Actual course-level competency names

`CSC370-01_ Welcome!-1.pdf`, slides 6-8, names **Data Analytics**, **Data Modelling**, and **Back-end Engineering**. The sprint plan uses these names.

| Competency | Meaning in the supplied lecture, paraphrased | Current project limitation | Measurable next-sprint improvement |
| --- | --- | --- | --- |
| Data Analytics | Use correct SQL, progressing to aggregation/subqueries and then efficient idiomatic queries; prepare analysis-ready results. The introductory transcript says visualization is out of scope | Seven verified basic reports; no comprehensive advanced query pack | S2-1 adds 8 advanced reports and labelled tabular/CSV output, all checked against expected rows. Charts and scaled performance experiments are optional |
| Data Modelling | Turn application requirements into normalized abstractions with clear conceptual/relational schemata and trustworthy populated instances | Current assumptions and synthetic fixture cover one student-facing workflow; future requirements could introduce new FDs/MVDs | S2-5 keeps the Chen diagram, relational model and FD/MVD decisions synchronized; rerun all coverage/key/normalization and migration checks; record fixture provenance and any new requirements |
| Back-end Engineering | Connect applications and databases using compatible API/SQL and appropriate access, consistency and concurrency controls | Integrity and rollback are tested, but reusable views and a documented multi-step transaction are missing | S2-3 adds two views and a SQL operation with success, induced-failure rollback and committed-read tests. APIs and restricted-account integration are optional later work; the introductory transcript presents an API as aspirational |

## Lecture-by-lecture mapping

| Supplied lecture and relevant slides | Lesson objective, paraphrased | Sprint 1 evidence | Next-sprint continuation |
| --- | --- | --- | --- |
| 01 Welcome, 4-8 | Name course goals | This matrix uses the actual three competency names | Explain how each next-sprint goal improves the named competency |
| 02 Storing Data w/ SQL, 3, 30-36 | Execute CREATE/ALTER statements and insert typed scalar values | schema.sql; current seed; tested `migrations/001_sprint1.sql` uses ALTER TABLE while preserving kick-off data | Clean-load and migration regression after schema changes |
| 03 Retrieving Data with SQL, 3, 9-22 | Retrieve data using simple SQL and relate it to selection/projection/rename/joins/set operations | Seven reports with exact expected rows; constraints use π, σ, ρ, difference and theta joins | S2-1 adds EXISTS, correlated queries, HAVING and set-operation reports, checking bag/NULL semantics |
| 04 Conceptual Design, 4, 6-10, 14-18, 23-28 | Construct a conceptual ERD using entity sets, attributes, identifiers, relationships and roles | CONCEPTUAL_ERD.svg uses the course's Chen-style notation; 50 descriptive attributes/identifiers plus relationships; relational diagram accounts for every SQL column | Regenerate both levels of model after changes |
| 05 Multiplicity, 3, 16-19, 22-32 | Determine binary/multi-way multiplicities and how they affect identifiers and table mapping | CONCEPTUAL_ERD.md maps every relationship and min/max participation; explains the student/posting association and why independent binary relationships suffice | Preserve relationship keys; test altered uniqueness if requirements change |
| 06 FD's & Keys, 4, 29, 34-49, 55-57 | Identify domain FDs, compute closures and determine keys/superkeys | NORMALIZATION.md states assumptions and all keys; exhaustive closure checks for all nine production relations | Re-evaluate keys whenever requirements add dependencies; do not infer FDs from coincidental seed patterns |
| 07 BCNF Decomposition, 4, 20, 24-30, 36-39 | Decompose using violating FDs and reconstruct through lossless joins | Resume-selection decomposition and worked Flat example; verified closure/intersection conditions | Retain dependency-preservation reasoning and exact migration tests |
| 08 Constraints in Relational Algebra, 3, 19-20, 39, 45, 50-58 | Express value, key, FD and referential integrity constraints algebraically | docs/CONSTRAINTS.md includes empty-result/subset rules and renamed self-join constraints; database checks exercise enforcement | Rerun all constraint counterexamples and translate any new cross-table rule carefully |
| 09 Weak Entity Sets & Inheritance, 3, 14-23, 25-27 | Simplify modelling through subsets and borrowed identifiers | Explicit Interview weak-entity alternative and chosen surrogate mapping; considered/rejected unnecessary posting inheritance; subtype PK/FK approach explained | Add a subtype only if distinct attributes or restricted relationships justify it |
| 10 Improving Conceptual Designs, 3, 11-13, 34-44 | Evaluate completeness, correctness, minimality, expressiveness, readability, self-explanation, extensibility and normality; classify transformations | docs/CONCEPTUAL_DESIGN_REVIEW.md applies every criterion to this tracker, including the conditional resume-owner cycle and preservation of legal states | S2-5 revisits each criterion after changes |
| 11 ERDs to FDs, 2, 4-8, 13-29 | Verify relational mappings, identifier FDs, relationship FDs and conceptual normality | Production table proofs plus explicit entity/link verification in the design-quality review; exact diagram/FK coverage checks | Reject multiplicities or identifiers inconsistent with changed domain FDs |
| 12 Projecting FDs, 3, 11-22, 29-38 | Compare FD-set closures, compute a minimal basis and project implied dependencies | Full projected closure table in NORMALIZATION.md; equivalence/minimality and every-subset projection tests | Recompute projected dependencies for every changed decomposition |
| 23 Third Normal Form - corrected, 3, 12-24 | Identify prime attributes, reason about dependency preservation and synthesize a lossless 3NF design | Allocation tradeoff plus a complete project-shaped synthesis requiring the added AQ key relation; executable preservation/normality/reconstruction checks | Reuse synthesis when preservation justifies 3NF; do not weaken already-BCNF production tables gratuitously |
| 24 4NF & MVDs, 4, 22, 26, 31-39 | Use the MVD tuple-swap definition, identify violations and recursively decompose into 4NF | Formal MVD tests, triviality/complementarity, a no-splitting counterexample and lossless independent-value decomposition | Review domain independence, not merely scalar SQL types or seed coincidences |

## Worksheets, transcripts and scope boundaries

The three worksheets are practice material: primary/foreign keys from ERDs, projected minimal bases, and 3NF synthesis. Their methods are applied to the tracker and to clearly labelled project-shaped experiments. The production schema retains the co-op tracking scope.

The introductory transcript is misleadingly named `CSC 485A_586F Lectur-transcript.txt`, but its opening and content explicitly identify CSC 370. It clarifies the competency progression and says visualization is outside scope; an API is an aspirational stage. Charts and an API are optional extensions in the plan. Transcript references to relative due dates are not used to infer this submission's deadline or replace the supplied assignment/rubric.

The added corrected 3NF deck resolves an inconsistent prime-key sentence in the 4NF deck's review: both city/title and theatre/title are keys in the cinema example. Closure calculations verify the result. The project does not repeat the inconsistent sentence.

Advanced SQL remains planned through joins, aggregates/HAVING, subqueries/EXISTS, set operations, views, NULL/bag semantics and SQL transaction operations. CTE/window work, a chart, API and performance experiments are optional extensions, not asserted official module requirements.

The practice-exam booklet, questions 16-21, reinforces project-specific reasoning about changed constraints, keys, multivalued facts and alternative conceptual designs. The booklet does not add its example domains to Sprint 1.

## Exact relational-algebra forms used for key/FD rules

Following lecture 08, rule statements in first-order logic can also be written as empty self-join results. With `a := ρ_a(Application)` and `b := ρ_b(Application)`:

`σ_(a.student_id=b.student_id ∧ a.posting_id=b.posting_id ∧ a.application_id≠b.application_id)(a × b) = ∅`.

This encodes the alternate application key. For Interview, replace the matched fields with application_id/interview_round and require distinct interview_id. For the Student FD student_id -> full_name, rename Student as s and t and require:

`σ_(s.student_id=t.student_id ∧ s.full_name≠t.full_name)(s × t) = ∅`.

The cross-table resume-ownership rule uses explicit theta joins on the reference keys, not a natural join that could discard violations by also joining on student_id. Optional values are discussed separately in NORMALIZATION.md.
