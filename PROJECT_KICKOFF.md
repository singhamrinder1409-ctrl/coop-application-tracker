# Project Kick-Off Report

## Project Title

Co-op Application Tracker

## Team

Group 3:

- Amrinder Singh
- Jaiman Singh
- Aashna Sadeque

## Project Direction

For our CSC 370 project, we decided to make a Co-op Application Tracker. The system is meant to help students keep track of job postings, employers, applications, interviews, and offers.

We think this topic works well because co-op applications can get hard to manage after a while. A student might apply to many jobs, one employer can post many jobs, and one application can move through different stages. To us, this is a real case where a database is better than one long spreadsheet.

## Main User

The main user for the first version is a student applying for co-op jobs. Later, the project could include an advisor or admin view, but we are not trying to build that yet.

## Main Features

- store students
- store employers
- store job postings
- track applications
- track the current application status
- track interview rounds
- track offers
- store resume versions used for applications
- run SQL queries about active applications, interviews, and offers

## Why This Fits The Course

In our view, this project fits CSC 370 because it uses the design ideas from the course in a direct way. We have entity sets, attributes, identifiers, relationships, multiplicities, keys, foreign keys, and SQL DDL.

The project also gives us normal database design problems to think about. For example, employer information should not be copied into every application row. If it was copied everywhere, changing an employer website would mean updating the same fact in many places.

## Current Sprint Goals

For this kick-off sprint, we treated the given starting plan as:

1. Make a clear project direction.
2. Make a conceptual design and ERD.
3. Convert the ERD into a relational schema.
4. Write MySQL DDL for a normalized database.
5. Explain the main keys, functional dependencies, and BCNF choices.

## Evidence Of Progress

We made these core files:

- `ERD.md`
- `RELATIONAL_SCHEMA.md`
- `NORMALIZATION.md`
- `SPRINT_PLAN.md`
- `schema.sql`
- `SOURCES.md`

Acc to us, this is enough evidence for the kick-off because the project now has a real database structure. The schema can be created in MySQL, and the design can be explained using course ideas.

## Course Connection

The project connects to the course goals in a direct way:

- We are modelling the world as data by turning co-op tracking into entity sets and relationships.
- We are building part of a back end by writing MySQL DDL and constraints.
- We are preparing to analyse data with SQL by designing tables that can be queried later.

The design also uses ideas from the slides, like conceptual design, identifiers, multiplicity, functional dependencies, keys, foreign keys, and BCNF decomposition.

## What Is Still Missing

We have not received any TA/client requirements yet. Because of that, the current scope is based on what we think a co-op tracker should need. If the TA wants something different, we can change the design in the next sprint.

We also still need to push the repo to GitHub and use the final GitHub link and commit hash in the Brightspace submission.

## Sources Used

The project was made using the CSC 370 kick-off instructions, the attached rubric, and the lecture slides up to Advanced Relational Design. More details are in `SOURCES.md`.
