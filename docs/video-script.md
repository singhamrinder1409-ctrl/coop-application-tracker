# Video Script And Outline

Group size is 3, so the video must be no longer than 11 minutes.

## Suggested Timing

### 0:00-0:45 - Introduction

Hi, we are Group 3. Our project is a Co-op Application Tracker. The goal is to help students track job postings, applications, interviews, employers, and offers in one database.

We chose this topic because co-op applications can get hard to manage if everything is stored in a spreadsheet. There are many connected pieces of data, so it fits a relational database project pretty well.

### 0:45-2:00 - Requirements And Scope

For this first version, the main user is a student. The student can track employers, job postings, applications, resume versions, interviews, and offers.

We kept the scope focused for now because this is the kick-off submission. We have not received TA-client requirements yet, so we expect the scope may change after feedback.

### 2:00-4:00 - ERD

Show `docs/erd.md`.

Our main entity sets are Student, Employer, JobPosting, Application, ApplicationStatus, ResumeVersion, Interview, and Offer.

Some important relationships are:

- one employer can post many jobs
- one student can submit many applications
- each application belongs to one student and one job posting
- one application can have many interviews
- one application can have at most one offer

We also gave each entity set an identifier, like `student_id`, `employer_id`, and `application_id`.

### 4:00-6:00 - Relational Schema And SQL DDL

Show `docs/relational-schema.md` and `sql/schema.sql`.

We converted the ERD into relational tables. The SQL file creates the database, tables, primary keys, foreign keys, unique constraints, and some check constraints.

For example, `Application` connects a student to a job posting and has a status. We also added a unique constraint on `(student_id, posting_id)` so one student cannot apply twice to the same job posting.

### 6:00-7:30 - Normalization And BCNF

Show `docs/normalization.md`.

We tried not to put all information into one big table because that would repeat employer and student data. It could cause update and deletion problems.

In our design, employer information is stored in `Employer`, posting information is stored in `JobPosting`, and application information is stored in `Application`. This makes the functional dependencies cleaner because most non-key attributes depend on the key of their own table.

### 7:30-9:00 - Demo Queries

Show `sql/demo_queries.sql`.

Some demo queries are:

- list all applications with employer and job title
- show active applications
- show upcoming interviews
- show offers
- count applications by status

These queries show that the database can already answer useful questions.

### 9:00-10:30 - Next Sprint Plan

Show `docs/sprint-plan.md`.

For the next sprint, we want to review the design with the TA-client, add more formal constraints, write relational algebra constraints, add better sample data, and prepare more queries.

This connects to Advanced Relational Design because we will focus more on constraints, referential integrity, and whether any weak entity set or inheritance pattern is useful.

### 10:30-11:00 - Closing

Overall, we think this is a good starting point because we have a clear topic, an ERD, a relational schema, SQL DDL, normalization notes, and a plan for improving the design in the next sprint.

