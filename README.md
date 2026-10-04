# Co-op Application Tracker

CSC 370 Project Kick-Off - Fall 2026

## Group 3

| Name | Username |
| --- | --- |
| Amrinder Singh | amrinder |
| Jaiman Singh | jaiman1 |
| Aashna Sadeque | aashnas |


## Project Idea

We are planning to build a Co-op Application Tracker. The main idea is to help students keep track of job postings, employers, applications, interviews, and offers in one database.

To us, this is a good database project because the information is connected in many ways. One employer can post many jobs. One student can apply to many jobs. One application can have interviews and maybe an offer. There are also useful constraints, like one student should not have two applications for the exact same job posting.

## Main Submission Files

These are the main files for the kick-off evidence:

- `PROJECT_KICKOFF.md`: project direction and progress report
- `ERD.md`: ERD notes and diagram
- `RELATIONAL_SCHEMA.md`: relational schema with keys and foreign keys
- `NORMALIZATION.md`: functional dependencies and BCNF notes
- `SPRINT_PLAN.md`: current sprint evidence and next sprint plan
- `schema.sql`: MySQL DDL code
- `SOURCES.md`: course sources used
- `supporting-files/seed.sql`: optional sample data for demo/testing
- `supporting-files/demo_queries.sql`: optional SQL queries for demo/testing

## How To Demo Locally

If MySQL is installed, run:

```bash
mysql -u root -p < schema.sql
mysql -u root -p coop_application_tracker < supporting-files/seed.sql
mysql -u root -p coop_application_tracker < supporting-files/demo_queries.sql
```

If you use a different MySQL username, change the command as needed.

## Submission Checklist

- Add these files to a GitHub repository.
- Commit the files.
- Copy the GitHub link and the exact commit hash.
- Record a video that is no longer than 11 minutes because the group has 3 people.
- In the video, show the ERD/schema, SQL DDL, evidence of progress, and next sprint plan.
- Make sure one group member submits on Brightspace for the whole group.
- If the GitHub repo is private, give access to the instructor and TA-client.
- Include or point to `SOURCES.md` so the course sources are clear.
