# Co-op Application Tracker

CSC 370 Project Kick-Off - Fall 2026

## Group

Group 3

| Name | Username |
| --- | --- |
| Amrinder Singh | amrinder |
| Jaiman Singh | jaiman1 |
| Aashna Sadeque | aashnas |

Student numbers can be added if Brightspace or the TA asks for them.

## Project Idea

We are planning to build a Co-op Application Tracker. The main idea is to help students keep track of job postings, employers, applications, interviews, and offers in one database.

To us, this is a good database project because the information is connected in many ways. One employer can post many jobs. One student can apply to many jobs. One application can have interviews and maybe an offer. There are also useful constraints, like one student should not have two applications for the exact same job posting.

## What Is In This Kick-Off Package

- `docs/kickoff-report.md`: written report for the kick-off submission
- `docs/erd.md`: ERD description and Mermaid diagram
- `docs/relational-schema.md`: relational schema with keys and foreign keys
- `docs/normalization.md`: functional dependencies and BCNF notes
- `docs/sprint-plan.md`: current sprint evidence and next sprint plan
- `docs/video-script.md`: suggested video outline/script
- `docs/ai-and-sources.md`: AI use and course source note
- `sql/schema.sql`: MySQL DDL code
- `sql/seed.sql`: sample data for demo
- `sql/demo_queries.sql`: SQL queries to show progress in the video

## How To Demo Locally

If MySQL is installed, run:

```bash
mysql -u root -p < sql/schema.sql
mysql -u root -p coop_application_tracker < sql/seed.sql
mysql -u root -p coop_application_tracker < sql/demo_queries.sql
```

If the group uses a different MySQL username, change the command as needed.

## Submission Checklist

- Add these files to a GitHub repository.
- Commit the files.
- Copy the GitHub link and the exact commit hash.
- Record a video that is no longer than 11 minutes because the group has 3 people.
- In the video, show the ERD/schema, SQL DDL, sample data, demo queries, and next sprint plan.
- Make sure one group member submits on Brightspace for the whole group.
- If the GitHub repo is private, give access to the instructor and TA-client.
- Include or point to `docs/ai-and-sources.md` so AI use and course sources are clear.
