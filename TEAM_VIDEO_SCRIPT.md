# Team Video Script

Group size is 3, so the video must be 11 minutes or less. A safe target is around 8-9 minutes.

## Speaker 1: Amrinder

Target time: 0:00-2:45

### Show

- `README.md`
- `PROJECT_KICKOFF.md`

### Say

Hi, we are Group 3. Our project is the Co-op Application Tracker. Our team members are Amrinder, Jaiman, and Aashna.

For this project, we decided to design a database system that helps students track their co-op applications. The system keeps information about students, employers, job postings, applications, interviews, resume versions, and offers.

We chose this topic because co-op applications can get hard to manage if everything is just kept in a spreadsheet. One student can apply to many jobs, one employer can post many jobs, and one application can go through different stages like applied, interview, rejected, or offer. To us, this makes it a good database project because the information is connected in many ways.

For this first version, our main user is a student applying for co-op jobs. We are not trying to build a full advisor or admin system yet. We think it is better to keep the first scope focused and then adjust it after TA-client feedback.

Our main goals for this sprint were to choose a clear project direction, make a conceptual design, create an ERD, convert it into a relational schema, write MySQL DDL, and explain the main normalization choices.

### Transition

Now Jaiman will go through the ERD and relational schema.

## Speaker 2: Jaiman

Target time: 2:45-5:45

### Show

- `ERD.svg`
- `ERD.md`
- `RELATIONAL_SCHEMA.md`
- `schema.sql`

### Say

This is our ERD diagram. The main entity sets are `Student`, `Employer`, `JobPosting`, `Application`, `ApplicationStatus`, `ResumeVersion`, `Interview`, and `Offer`.

We gave each entity an identifier. For example, `Student` has `student_id`, `Employer` has `employer_id`, and `Application` has `application_id`.

Some of the important relationships are that one employer can have many job postings, one student can submit many applications, and each application belongs to one student and one job posting. Also, one application can have many interviews, but in our first design one application can have at most one offer.

The ERD is shown in a Chen-style format like the lecture slides. Rectangles are entity sets, ellipses are attributes, diamonds are relationships, and the underlined attributes are identifiers.

After that, we converted the ERD into a relational schema. In `RELATIONAL_SCHEMA.md`, we list the tables and show the primary keys and foreign keys.

Now in `schema.sql`, we implemented the design in MySQL. The file creates the database and tables. It also includes primary keys, foreign keys, unique constraints, and some check constraints. For example, the `Application` table has a unique constraint on `student_id` and `posting_id`, so the same student cannot apply twice to the exact same posting.

### Transition

Now Aashna will explain the normalization work and our next sprint plan.

## Speaker 3: Aashna

Target time: 5:45-8:45

### Show

- `NORMALIZATION.md`
- `SPRINT_PLAN.md`
- `SOURCES.md`
- optional: `supporting-files/demo_queries.sql`

### Say

For normalization, we first thought about what would happen if we kept everything in one big table. That might look simple, but it would repeat a lot of information. For example, the same employer name and website could appear in many application rows.

This could cause update, insertion, and deletion problems. If an employer website changed, we might have to update it in many places. If we deleted one application, we also do not want to accidentally lose information about the employer or job posting.

So in our design, employer information is stored in `Employer`, job posting information is stored in `JobPosting`, student information is stored in `Student`, and application information is stored in `Application`.

We also wrote out the main functional dependencies. For example, `student_id` determines the student information, `employer_id` determines the employer information, and `application_id` determines the information for one application.

Acc to us, the design is close to BCNF because the important facts are separated into their own tables, and the non-key attributes depend on the key of that table.

For the next sprint, we plan to review the schema with our TA-client and update it based on feedback. We also want to add more formal constraints, write some relational algebra constraints, add better sample data, and write more SQL queries.

This connects to Advanced Relational Design because we will focus more on constraints, referential integrity, and whether weak entity sets or inheritance are useful for our project.

We also included `SOURCES.md`, which lists the course instructions, rubric, and lecture slides we used.

### Closing

Overall, we think this is a good starting point because we have a clear project direction, an ERD, a relational schema, MySQL DDL, normalization notes, and a plan for the next sprint.

## Optional Demo If There Is Time

Target time: 8:45-10:30

### Show

- `supporting-files/seed.sql`
- `supporting-files/demo_queries.sql`

### Say

We also made optional sample data and demo queries. These are not the main required files, but they help show that the database can answer useful questions.

For example, the demo queries can show all applications with employer and job title, active applications, upcoming interviews, application counts by status, and offers with deadlines.

This helps us show that the schema is usable and not just a diagram.

## Final Reminder

Do not go over 11 minutes. If the video is getting long, skip the optional demo section and just mention that the files are included in `supporting-files`.
