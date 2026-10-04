# Project Kick-Off Report

## Project Title

Co-op Application Tracker

## Team

Group 3:

- Amrinder Singh
- Jaiman Singh
- Aashna Sadeque

## Project Direction

For our CSC 370 project, we decided to make a Co-op Application Tracker. The system will store information about students, employers, job postings, applications, interviews, and offers.

We think this topic makes sense because co-op applications usually become messy after a while. A student might apply to many jobs, each job belongs to an employer, and each application can move through different stages like saved, applied, interview, rejected, or offer. It seems like a real case where a relational database can help because the data should not just be kept in one big spreadsheet.

## Main Users

The main user is a student who is applying for co-op jobs. In our first version, we are focusing on a student tracking their own applications. Later, this could be extended so an advisor or admin can view progress, but that is not part of the first scope.

## Main Features We Want To Support

- store student profile information
- store employers and their basic details
- store job postings from employers
- track applications submitted by students
- track application status
- track interview rounds for an application
- track offers connected to applications
- store resume versions used for different applications
- run SQL queries to answer useful questions, like which applications are still active

## Why This Is A Good Database Project

In our view, this project fits the course because it needs conceptual design, relational design, SQL DDL, keys, foreign keys, and normalization. It also has different relationship types:

- one employer can have many job postings
- one student can submit many applications
- one job posting can receive applications from many students
- one application can have many interviews
- one application can have at most one offer in our first design

This gives us enough room to show ERD design, multiplicities, relational schema mapping, and BCNF reasoning without making the project too large for the first sprint.

## Current Sprint Goals

For this kick-off sprint, we are treating the given starting plan as:

1. Create a conceptual design for the project.
2. Build an ERD with entity sets, attributes, identifiers, relationships, and multiplicities.
3. Convert the ERD into a relational schema.
4. Write SQL DDL code to create a normalized MySQL database.
5. Explain the main functional dependencies and why the design avoids common anomalies.

## Evidence Of Progress

We made the following files as evidence:

- `docs/erd.md` shows the conceptual design and ERD.
- `docs/relational-schema.md` shows the relational schema.
- `docs/normalization.md` explains keys, functional dependencies, and BCNF.
- `sql/schema.sql` contains the MySQL `CREATE TABLE` statements.
- `sql/seed.sql` contains sample data.
- `sql/demo_queries.sql` contains example queries we can run in the video.

Acc to us, this is enough evidence for the kick-off because it shows the project idea is not just a vague topic anymore. It has a database structure and some SQL that can be tested.

## Course Connection

The project connects to the course goals in a direct way:

- We are modelling the world as data by turning co-op tracking into entity sets and relationships.
- We are building the back-end part by writing MySQL DDL and constraints.
- We are preparing to analyse data with SQL by adding demo queries for applications, interviews, and offers.

The design also uses ideas from the slides, like conceptual design, identifiers, multiplicity, functional dependencies, keys, foreign keys, and BCNF decomposition. We tried to avoid putting everything in one table because that would create repeated data and update problems.

## What Is Still Missing

We have not received any TA/client requirements yet. Because of that, the current scope is based on what we think a student co-op tracker should need. If the TA wants a different user role or extra feature, we can adjust the schema in the next sprint.

We also need to add the final GitHub repository link and exact commit hash after the files are pushed.

