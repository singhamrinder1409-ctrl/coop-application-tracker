# Conceptual design quality review

We evaluated the tracker together using eight conceptual-design quality criteria. The review covers the student-facing tracker scope.

| Criterion | Review of this project | Change / observable evidence |
| --- | --- | --- |
| Completeness | Student-facing scope requires postings/employers, applications/statuses, resume choices, multiple interview rounds and optional offers. Employer/advisor accounts and real recruitment feeds were not promised | Every scoped feature maps to an entity/relationship, SQL schema and fixture or workflow check. Both diagrams cover all attributes or their relationship mappings |
| Correctness | Use Chen entities, ellipses, identifiers and diamonds; distinguish conceptual links from SQL FK columns. An application may select zero or one resume, and a resume may serve multiple applications | CONCEPTUAL_ERD.md lists participation and mappings; schema uniqueness and optional assignment relation match these choices; tests reject inconsistent ownership |
| Minimality | Do not store application_count, interview_count or employer name copies on Application. Counts are derived by queries. The student/application/resume cycle is only conditionally redundant | Application.student_id remains necessary when no resume is selected. For assigned resumes, ownership is constrained to agree; the cross-table rule is explicit. Removing the application owner globally would lose saved applications' ownership |
| Expressiveness | Application has a lifecycle and relationships to interviews/offers, so a named entity is useful. ApplicationStatus has a terminal-state property and shared use; it is not an unexplained one-attribute entity | Keep the application/status entities. Avoid remote/on-site subtype tables without subtype-specific attributes or relationships |
| Readability | Every attribute is present, identifiers are underlined and graph edges do not cross in the current layouts. Attribute panels and relationship view refer to the same named entities | Visually inspected conceptual and relational SVGs. Panels are separate views of the same entities, not separate duplicated facts. Use the relational diagram for SQL-level detail |
| Self-explanation | Names, participation labels and the legend explain basic relationships. Ownership and immutable-owner policies require an extra constraint beyond binary multiplicities | Explain these rules in docs/CONSTRAINTS.md and the video; do not claim arrows alone express them. The min/max convention is stated separately from crow's-foot endpoints |
| Extensibility | Employer and posting facts are separate. New interview rounds are rows; new status labels are lookup rows. A new independent skill/city requirement can be added with separate relations | Existing key and migration tests demonstrate local changes while retaining old records. Revisit the one-offer assumption explicitly if offer revisions become a requirement |
| Normality | Entity identifiers must really determine all their descriptive attributes; relationship multiplicities must agree with domain FDs | NORMALIZATION.md checks every table, ERD-implied FDs, minimal bases and projected FDs. A declared FD model and MVD assumptions are stated separately from sample-data checks |

## Changes and their effect on stored information

- Completing the attribute drawing is an information-preserving documentation correction: the omitted columns already existed in the kick-off DDL.
- Splitting selected-resume assignment from Application is information-preserving **for legal same-owner states**, with a lossless assigned-resume fragment and a tested migration. It also restricts permitted states: cross-student selections and NULL priority are now rejected. A legacy row that violates these rules needs correction before migration.
- Moving resume selection to its own relationship preserves the distinction between “no selection” and a real assigned resume; applications without a selection still keep their student owner.
- The extra fixture rows and two new reports increase demonstration evidence; they do not add a new domain requirement.
- Avoiding unnecessary subtypes prevents extra structure without deleting a requirement. The current implementation uses a location-type discriminator.

## Check relationships against functional dependencies

For each strong entity, its chosen ID determines every descriptive attribute. Many-to-one links imply child ID -> parent ID; examples are posting_id -> employer_id and application_id -> posting_id/student_id/status_id. “For” must therefore not be drawn as many-to-many. The zero-or-one offer relation gives both application_id -> offer_id and offer_id -> application_id in Offer. Uses of a selected resume imply application_id -> resume_id, while resume_id -> application_id is false because reuse is allowed.

The student/posting pair is an alternate key of Application; neither student nor posting alone identifies an application. The many-to-many association is therefore mediated by the application entity and its lifecycle attributes. The separate conceptual student, posting and employer facts must not be collapsed into one entity merely because identifiers link them; doing so would repeat facts determined by non-key attributes.
