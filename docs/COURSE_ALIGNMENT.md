# Course competency alignment

This connects the delivered Sprint 2 work and the proposed Sprint 3 work to Data Analytics, Data Modelling and Back-end Engineering. Source references are in SOURCES.md. Current scope is through Advanced SQL; the next scope is through Analysing Query Algorithms.

| Competency | Sprint 2 improvement | Remaining limitation | Measurable Sprint 3 goal |
| --- | --- | --- | --- |
| Data Analytics | Eight advanced reports and four query-equivalence pairs, with independently expected results for NULLs, duplicate-producing joins and empty groups | Correctness is tested on a small fixture; equivalent forms have not been compared at scale | S3-1 and S3-4 add three controlled dataset sizes, require equal outputs, then save five measured runs and medians for equivalent forms |
| Data Modelling | Original nine-table model retained; views count children before joining; original keys/normalization/diagram checks still pass | Larger or skewed fixtures could reveal overlooked data assumptions | S3-1 verifies all fixture constraints and independent totals; S3-5 reruns every current verifier after any schema/index change |
| Back-end Engineering | Two invoker-security views and a standalone transaction with error rollback and committed reads from new connections | No query-algorithm cost model, physical-plan comparison, crash test or full concurrency benchmark | S3-2 and S3-3 state page-I/O/memory/cardinality assumptions, work four operator examples, compare join models and inspect three queries at three scales |

## Advanced SQL coverage

The topic matrix in SPRINT_PLAN.md maps INNER/LEFT JOIN, WHERE/GROUP BY/HAVING, correlated and nested subqueries, EXISTS/NOT EXISTS, relational division, UNION, bag/NULL semantics, views and transaction behavior to named SQL and tests. Optional CTE/window work is completed separately. `docs/ADVANCED_SQL.md` explains each report's result and the transaction boundary. `evidence/sprint2/README.md` indexes the outputs.

## Relational design carried forward

The complete conceptual and relational diagrams still cover eight entity sets, nine base tables and all 59 SQL columns. Original proofs/checks for identifiers, multiplicities, FDs, keys, minimal bases, projection, BCNF, 3NF and MVD/4NF examples remain applicable. The ten algebra/SQL rules, Interview weak-entity alternative, inheritance decision and eight design-quality criteria are retained in the design documents. Sprint 2 adds no stored relation or attribute; it adds derived views and a transaction over the existing model.

## Query-algorithm scope planned next

The Sprint 3 matrix covers selection, projection/duplicate elimination, sorting, join algorithms, access paths, cardinality/selectivity, buffer limits and equivalent-query cost comparisons. Worked page-I/O models and actual MySQL plans are separate evidence. Timing claims require result equality and repeated measurements first. Existing PK/FK indexes are inspected before adding candidates; a full scan or unsuccessful index experiment is reported rather than hidden.

No extra official Advanced SQL or query-algorithm topic list was supplied. These detailed mappings and experiments are explicit project coverage under the assignment's named modules, not quotations of an unseen list. The unchanged earlier report is in `docs/archive/SPRINT1_REPORT_AND_PLAN.md`.

## Relational-algebra examples retained

With `a := ρ_a(Application)` and `b := ρ_b(Application)`, application uniqueness is:

`σ_(a.student_id=b.student_id ∧ a.posting_id=b.posting_id ∧ a.application_id≠b.application_id)(a × b) = ∅`.

The Student FD student_id -> full_name can be expressed using renamed copies s and t:

`σ_(s.student_id=t.student_id ∧ s.full_name≠t.full_name)(s × t) = ∅`.

The cross-table resume-ownership rule uses explicit joins on application_id and resume_id. A natural join on both student_id columns could discard the mismatches it is meant to detect. Optional-value qualifications are in NORMALIZATION.md.
