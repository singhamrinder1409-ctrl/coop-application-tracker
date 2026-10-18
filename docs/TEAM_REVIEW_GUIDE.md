# Team rehearsal and understanding guide

Use these questions to rehearse the video and explain the project’s design decisions individually.

Each member should be able to use the real files and explain:

1. Which original kick-off goals were delivered, and where the evidence is. Start with SPRINT_PLAN.md and the archived original plan.
2. How to read the Chen diagram's identifiers and participation, and why the relational diagram has a ninth table for the selected-resume relationship.
3. Why a resume's owner creates a BCNF problem in the assigned-resume fragment, why the decomposition is lossless, and why an unassigned application still needs its own student.
4. Why a nullable UNIQUE email is not treated as an unconditional classical candidate key, and which alternate keys the real tables have.
5. How to compute one closure, remove a redundant FD and project a dependency through an attribute absent from the projection. Trace the complete table in NORMALIZATION.md.
6. Why 3NF and BCNF differ, which attributes are prime in the Allocation example, and why the cinema review sentence is corrected by a closure calculation.
7. Why 3NF synthesis sometimes needs an added key relation. Explain which incorrect application/snippet pairings can arise if AQ is omitted.
8. What the MVD tuple-swap rule requires, why independent skill/city values need all four combinations, and why MVDs cannot use the FD splitting rule blindly.
9. How the eight conceptual-quality criteria apply to this specific tracker. Explain a tradeoff, not just the criterion names.
10. What an ownership trigger rejects, why the algebra must use explicit join predicates, and what the database tests actually establish about transactions.
11. How the two new reports differ from the five kick-off reports, including why COUNT(child_id) is needed for a student with no applications.
12. How to migrate the old fixture without losing assignments, and why MySQL DDL does not make the whole migration atomic.

Run the five verification commands in README.md and inspect their outputs. Explain an expected failure as well as a successful workflow. A passing test log demonstrates the test run, not individual understanding, a recorded video, a published repository, full ACID certification or an approved TA review.

For the recording, use TEAM_VIDEO_SCRIPT.md as an outline, adapt the wording to your own understanding, show real evidence and measure the exported duration. Do not claim that any member performed a particular step unless that is accurate.

## Practice-exam style changes

Use the practice booklet's project-question format to rehearse changes to this tracker:

- If multiple offers per application became valid, identify the affected UNIQUE constraint, cardinality and candidate-key claim. Give two rows that the revised model would accept and the present model would reject.
- List the FDs implied by the Employer and JobPosting entities and their relationship. Separate implications of identifiers from implications of multiplicity.
- If a student could record multiple independent preferred cities and skills, draw the change and explain the MVD decomposition without inserting comma-separated lists.
- Compare Application as an entity with a student/posting relationship carrying lifecycle attributes. Use the design criteria and its links to Interview and Offer to justify a choice.

These are preparation questions. Changes proposed in the practice exam are not requirements to implement in the submitted tracker.
