# Sprint Plan

## Current Sprint Goals

For this kick-off sprint, we worked from the course's given starting plan:

1. Develop a conceptual schema from our own requirements.
2. Create an ERD with entity sets, attributes, identifiers, relationships, and multiplicities.
3. Convert the ERD into a relational schema.
4. Implement the design as a normalized MySQL database using SQL DDL.

## Success Criteria For This Sprint

We consider this sprint successful if:

- the project topic is clear
- the ERD has the main entities and relationships
- each entity has an identifier
- the relationships have reasonable multiplicities
- the relational schema has primary keys and foreign keys
- the SQL DDL can create the database tables
- the design has some explanation of functional dependencies and BCNF

## Evidence That We Met The Goals

- The ERD is in `docs/erd.md`.
- The relational schema is in `docs/relational-schema.md`.
- The normalization reasoning is in `docs/normalization.md`.
- The MySQL DDL is in `sql/schema.sql`.
- The sample data is in `sql/seed.sql`.
- Demo SQL queries are in `sql/demo_queries.sql`.

We think this shows real progress because the project now has a structure that can be tested and changed. It is not just an idea anymore.

## Missed Or Uncertain Goals

We have not received TA/client requirements yet, so the scope is based on our current understanding. This means the design may change after we talk to the TA-client.

We also have not built an application UI yet. For this sprint, we focused on the database design because the instructions said to cover conceptual and relational schema design up to BCNF normalization.

## Plan For Next Sprint

For the next sprint, we want to cover the material up to Advanced Relational Design. Our plan is:

1. Review the schema with the TA-client and adjust the scope.
2. Add more formal constraints for data quality, including referential integrity and value constraints.
3. Write relational algebra constraints for some rules, such as:
   - every application must refer to an existing student and job posting
   - an application deadline should not be before the posting date
   - one application should not have duplicate interview round numbers
4. Decide whether any inheritance or weak entity set pattern is useful.
5. Add more realistic sample data.
6. Write more SQL queries for reporting, like active applications, interview schedule, and offers.
7. Start a small backend/API plan if the TA agrees that the database design is ready.

## Next Sprint Success Criteria

By the end of the next sprint, we should be able to show:

- an updated schema based on feedback
- at least five clear constraints written in SQL or relational algebra
- explanation of any advanced design choice, like weak entities or inheritance, if we use it
- sample data that covers normal cases and edge cases
- SQL queries that answer useful questions about co-op applications
- a short demo proving the database can support the main workflow

## Course-Level Connection

This next sprint connects to:

- data modelling, because we will improve the schema and constraints
- SQL/data analysis, because we will write more useful queries
- back-end engineering, because constraints and referential integrity make the database safer for an application to use

