# Team Video Script

Group size is 3, so the video must be 11 minutes or less. A safe target is around 9-10 minutes.

This script is written so the speaking and showing parts are split almost equally between the three members.

## Speaker 1: Amrinder

Target time: 0:00-3:10

### Show

- `README.md`
- `PROJECT_KICKOFF.md`
- project folder structure

### Say

Hi, we are Group 3. Our project is the Co-op Application Tracker. Our team members are Amrinder, Jaiman, and Aashna.

For this project, we decided to design a database system for students who are applying to co-op jobs. The main idea is to keep job postings, applications, interviews, employers, resume versions, and offers in one organized system.

We chose this topic because co-op applications can become messy pretty quickly. A student might apply to many jobs at the same time, and each job can have different deadlines, statuses, interviews, and possible offers. If all of this is only tracked in a spreadsheet, it is easy to lose context or repeat the same information many times.

This fits well as a database project because the data is connected. For example, one employer can post many jobs, one student can submit many applications, and one application can be linked to interviews, a resume version, and maybe an offer.

For the first version, our main user is a student. We are not building a full system for co-op advisors or employers yet. We kept the scope smaller because this is the kick-off stage, and we have not received TA-client requirements yet. Once we get feedback, we can adjust the design.

Our main sprint goals were to pick a clear project idea, write the project scope, create the ERD, convert the ERD into a relational schema, write the MySQL DDL, and explain the normalization choices up to BCNF.

In `PROJECT_KICKOFF.md`, we also explain our assumptions. For example, we assume that one application belongs to one student and one job posting. We also assume that an application can have multiple interviews, because some jobs have more than one interview round.

At this stage, the project is a good size. It is not too small, because there are enough entity sets and relationships to design properly. But it is also not too big for the first submission.

### Transition

Now Jaiman will go through the ERD and the relational schema.

## Speaker 2: Jaiman

Target time: 3:10-6:35

### Show

- `ERD.svg`
- `ERD.md`
- `RELATIONAL_SCHEMA.md`
- `schema.sql`

### Say

This is our ERD diagram. We made it in a Chen-style format like the lecture slides. Rectangles are entity sets, ellipses are attributes, diamonds are relationships, and the underlined attributes are identifiers.

The main entity sets are `Student`, `Employer`, `JobPosting`, `Application`, `ApplicationStatus`, `ResumeVersion`, `Interview`, and `Offer`.

Each entity set has an identifier. For example, `Student` has `student_id`, `Employer` has `employer_id`, `JobPosting` has `posting_id`, and `Application` has `application_id`.

Some of the relationships are simple but important. One student can submit many applications. One employer can post many job postings. Each application is for one job posting, and it also has one current status. An application can have many interviews, because there may be first round and second round interviews. Also, in our first design, an application may receive zero or one offer.

We also included resume versions because students often use different resumes for different jobs. So an application can use one resume version, and a student can own many resume versions.

After making the ERD, we converted it into a relational schema. In `RELATIONAL_SCHEMA.md`, we list the tables and show the keys and references. This helped us check if the ERD could actually become relational tables.

In `schema.sql`, we implemented the design in MySQL. The SQL file creates the database and all the tables. It includes primary keys, foreign keys, unique constraints, and check constraints.

One example is the `Application` table. It connects `Student`, `JobPosting`, `ApplicationStatus`, and `ResumeVersion`. We also added a unique constraint on `student_id` and `posting_id`. This means the same student should not apply twice to the exact same posting.

Another example is the `Interview` table. It has a foreign key to `Application`, so interviews cannot exist without being connected to an application. This makes sense for our project because an interview is part of the application process.

This schema is clear for the kick-off submission, but it is still flexible. If the TA-client says we need more details, like contacts, notes, or employer locations, we can add those later.

### Transition

Now Aashna will explain the normalization work, sources, and next sprint plan.

## Speaker 3: Aashna

Target time: 6:35-9:55

### Show

- `NORMALIZATION.md`
- `SPRINT_PLAN.md`
- `SOURCES.md`
- optional: `supporting-files/demo_queries.sql`

### Say

For normalization, we first thought about what would happen if everything was stored in one big table. At first, that might look easier, but it would repeat a lot of data.

For example, the same employer name and website could show up again and again for different job postings and applications. Student information could also repeat across many applications. This can cause problems when data changes.

If an employer website changes, we do not want to update it in many different rows. If a student deletes one application, we also do not want to accidentally lose employer or job posting information. These are the kinds of issues we were trying to avoid.

So we separated the data into tables based on what each table is actually about. Employer information is stored in `Employer`. Job posting information is stored in `JobPosting`. Student information is stored in `Student`. Application-specific information is stored in `Application`.

We also wrote out the main functional dependencies in `NORMALIZATION.md`. For example, `student_id` determines the student information, `employer_id` determines the employer information, and `application_id` determines the details for one application.

The design is close to BCNF because the main facts are separated into their own tables, and the non-key attributes depend on the key of that table. If we find a table later where some non-key attribute determines another non-key attribute, then we would need to split it more.

We also included `SOURCES.md`. That file lists the assignment instructions, rubric, and lecture slides we used while making this submission. We used the slides mainly to guide the ERD style, relational schema conversion, and normalization thinking.

For the next sprint, our plan is to review the schema with the TA-client, update the requirements, and improve the constraints. We also want to write relational algebra constraints and add better sample data.

This connects to Advanced Relational Design because we will be thinking more carefully about constraints, referential integrity, and whether ideas like weak entity sets or inheritance are useful for this project.

If there is time in the video, we can also quickly show the optional demo queries. These queries show examples like listing applications with employer and job title, showing active applications, showing upcoming interviews, counting applications by status, and showing offers.

Overall, this is a strong starting point for the project. We have a clear topic, an ERD, a relational schema, MySQL DDL, normalization notes, sources, and a plan for what to improve next.

## Optional Demo If There Is Time

Target time: 9:55-10:45

### Show

- `supporting-files/seed.sql`
- `supporting-files/demo_queries.sql`

### Say

We also made optional sample data and demo queries. These are not the main required files, but they help show that the schema can answer useful questions.

For example, the demo queries can show all applications with employer and job title, active applications, upcoming interviews, application counts by status, and offers with deadlines.

This helps us show that the schema is usable and not just a diagram.

## Final Reminder

Do not go over 11 minutes. If the video is getting long, skip the optional demo section and only mention that the files are included in `supporting-files`.
