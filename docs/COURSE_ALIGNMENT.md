# Course competency alignment

This maps course competencies and topics to our shared Sprint 1 work and next-sprint goals. Current coverage extends through Advanced Relational Design; the next plan covers the Advanced SQL operations listed below.

## Course-level competencies

Our plan addresses **Data Analytics**, **Data Modelling** and **Back-end Engineering**. Source references are listed in SOURCES.md.

| Competency | Competency focus | Current project limitation | Measurable next-sprint improvement |
| --- | --- | --- | --- |
| Data Analytics | Use correct SQL, progressing to aggregation/subqueries and then efficient idiomatic queries; prepare analysis-ready results | Seven verified basic reports; no comprehensive advanced query pack | S2-1 adds 8 advanced reports and labelled tabular/CSV output, all checked against expected rows. Charts and scaled performance experiments are optional |
| Data Modelling | Turn application requirements into normalized abstractions with clear conceptual/relational schemata and trustworthy populated instances | Current assumptions and synthetic fixture cover one student-facing workflow; future requirements could introduce new FDs/MVDs | S2-5 keeps the Chen diagram, relational model and FD/MVD decisions synchronized; rerun all coverage/key/normalization and migration checks; record fixture provenance and any new requirements |
| Back-end Engineering | Connect applications and databases using compatible API/SQL and appropriate access, consistency and concurrency controls | Integrity and rollback are tested, but reusable views and a documented multi-step transaction are missing | S2-3 adds two views and a SQL operation with success, induced-failure rollback and committed-read tests. APIs and restricted-account integration are optional later work |

## Topic coverage

| Course topic | Learning objective | Sprint 1 evidence | Next-sprint continuation |
| --- | --- | --- | --- |
| Welcome | Name course goals | This matrix uses the actual three competency names | Explain how each next-sprint goal improves the named competency |
| Storing Data w/ SQL | Execute CREATE/ALTER statements and insert typed scalar values | schema.sql; current seed; saved migration results demonstrate preservation of kickoff data | Clean-load and migration regression after schema changes |
| Retrieving Data with SQL | Retrieve data using simple SQL and relate it to selection/projection/rename/joins/set operations | Seven reports with exact expected rows; constraints use π, σ, ρ, difference and theta joins | S2-1 adds EXISTS, correlated queries, HAVING and set-operation reports, checking bag/NULL semantics |
| Conceptual Design | Construct a conceptual ERD using entity sets, attributes, identifiers, relationships and roles | CONCEPTUAL_ERD.svg uses the course's Chen-style notation; 50 descriptive attributes/identifiers plus relationships; relational diagram accounts for every SQL column | Regenerate both levels of model after changes |
| Multiplicity | Determine binary/multi-way multiplicities and how they affect identifiers and table mapping | CONCEPTUAL_ERD.md maps every relationship and min/max participation; explains the student/posting association and why independent binary relationships suffice | Preserve relationship keys; test altered uniqueness if requirements change |
| FD's & Keys | Identify domain FDs, compute closures and determine keys/superkeys | NORMALIZATION.md states assumptions and all keys; exhaustive closure checks for all nine production relations | Re-evaluate keys whenever requirements add dependencies; do not infer FDs from coincidental seed patterns |
| BCNF Decomposition | Decompose using violating FDs and reconstruct through lossless joins | Resume-selection decomposition and worked Flat example; verified closure/intersection conditions | Retain dependency-preservation reasoning and exact migration tests |
| Constraints in Relational Algebra | Express value, key, FD and referential integrity constraints algebraically | docs/CONSTRAINTS.md includes empty-result/subset rules and renamed self-join constraints; database checks exercise enforcement | Rerun all constraint counterexamples and translate any new cross-table rule carefully |
| Weak Entity Sets & Inheritance | Simplify modelling through subsets and borrowed identifiers | Explicit Interview weak-entity alternative and chosen surrogate mapping; considered/rejected unnecessary posting inheritance; subtype PK/FK approach explained | Add a subtype only if distinct attributes or restricted relationships justify it |
| Improving Conceptual Designs | Evaluate completeness, correctness, minimality, expressiveness, readability, self-explanation, extensibility and normality; classify transformations | docs/CONCEPTUAL_DESIGN_REVIEW.md applies every criterion to this tracker, including the conditional resume-owner cycle and preservation of legal states | S2-5 revisits each criterion after changes |
| ERDs to FDs | Verify relational mappings, identifier FDs, relationship FDs and conceptual normality | Production table proofs plus explicit entity/link verification in the design-quality review; exact diagram/FK coverage checks | Reject multiplicities or identifiers inconsistent with changed domain FDs |
| Projecting FDs | Compare FD-set closures, compute a minimal basis and project implied dependencies | Full projected closure table in NORMALIZATION.md; equivalence/minimality and every-subset projection tests | Recompute projected dependencies for every changed decomposition |
| Third Normal Form - corrected | Identify prime attributes, reason about dependency preservation and synthesize a lossless 3NF design | Allocation tradeoff plus a complete project-shaped synthesis requiring the added AQ key relation; executable preservation/normality/reconstruction checks | Reuse synthesis when preservation justifies 3NF; do not weaken already-BCNF production tables gratuitously |
| 4NF & MVDs | Use the MVD tuple-swap definition, identify violations and recursively decompose into 4NF | Formal MVD tests, triviality/complementarity, a no-splitting counterexample and lossless independent-value decomposition | Review domain independence, not merely scalar SQL types or seed coincidences |

## Scope

Worked examples illustrate design methods without adding unrelated application features. Advanced SQL is planned through joins, aggregation/HAVING, subqueries/EXISTS, set operations, views, NULL/bag semantics and transactions. CTE/window work, charts, an API and performance experiments are optional extensions. References and source qualifications are kept in SOURCES.md.

## Exact relational-algebra forms used for key/FD rules

Rule statements in first-order logic can also be written as empty self-join results. With `a := ρ_a(Application)` and `b := ρ_b(Application)`:

`σ_(a.student_id=b.student_id ∧ a.posting_id=b.posting_id ∧ a.application_id≠b.application_id)(a × b) = ∅`.

This encodes the alternate application key. For Interview, replace the matched fields with application_id/interview_round and require distinct interview_id. For the Student FD student_id -> full_name, rename Student as s and t and require:

`σ_(s.student_id=t.student_id ∧ s.full_name≠t.full_name)(s × t) = ∅`.

The cross-table resume-ownership rule uses explicit theta joins on the reference keys, not a natural join that could discard violations by also joining on student_id. Optional values are discussed separately in NORMALIZATION.md.
