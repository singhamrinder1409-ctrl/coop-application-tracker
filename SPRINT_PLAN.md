# Sprint Plan

## Current Sprint Goals

For this kick-off sprint, we worked from the starting plan in the project instructions:

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

| Sprint goal | Evidence in the repo |
| --- | --- |
| Develop a conceptual schema | `ERD.md` explains the entity sets, identifiers, relationships, and multiplicities. |
| Create a complete ERD | `ERD.svg` shows the rendered ER diagram in Chen-style notation. |
| Convert the ERD into relations | `RELATIONAL_SCHEMA.md` lists the tables, keys, references, and uniqueness rules. |
| Implement a normalized database | `schema.sql` creates the MySQL database with tables, keys, foreign keys, and checks. |
| Explain functional dependencies and BCNF | `NORMALIZATION.md` lists the main FDs and explains why the tables were split. |
| Show the schema can support useful queries | `supporting-files/seed.sql` and `supporting-files/demo_queries.sql` give optional test data and demo queries. |

We think this shows real progress because the project now has a structure that can be tested and changed. It is not just an idea anymore.

## Missed Or Uncertain Goals

We have not received TA/client requirements yet, so the scope is based on our current understanding. This means the design may change after we talk to the TA-client.

We also have not built an application UI yet. We think that is okay for this sprint because the given kick-off plan focuses on conceptual design, relational schema design, SQL DDL, and normalization up to BCNF.

## Plan For Next Sprint

For the next sprint, we want to cover the material up to Advanced Relational Design. Our plan is:

1. Review the schema with the TA-client and adjust the scope.
2. Add more formal constraints for data quality, including referential integrity, value constraints, and the rule that an application's resume should belong to the same student.
3. Write relational algebra constraints for some rules, such as:
   - every application must refer to an existing student and job posting
   - an application deadline should not be before the posting date
   - one application should not have duplicate interview round numbers
4. Decide whether inheritance or weak entity sets would actually help our design.
5. Add more realistic sample data.
6. Write more SQL queries for reporting, like active applications, interview schedule, and offers.

## Next Sprint Success Criteria

By the end of the next sprint, we should be able to show:

- an updated schema based on feedback
- at least five clear constraints written in SQL or relational algebra
- explanation of any advanced design choice, like weak entities or inheritance, if we use one
- sample data that covers normal cases and edge cases
- SQL queries that answer useful questions about co-op applications
- a short demo proving the database can support the main workflow

## Course-Level Connection

This next sprint connects to the course in these ways:

- data modelling, because we will improve the schema and constraints
- SQL/data analysis, because we will write more useful queries
- back-end engineering, because constraints and referential integrity make the database safer for an application to use
- Advanced Relational Design, because we will decide whether weak entity sets, inheritance, and extra constraints are actually useful for this project
