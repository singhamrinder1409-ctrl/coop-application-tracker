# Normalization Notes

## Starting Point

If we made this project as one big table, it might look like this:

`CoopTracker(student_name, username, employer_name, employer_website, job_title, deadline, status_name, resume_file, interview_round, interview_time, offer_wage)`

At first this looks simple, but it would repeat a lot of data. The same employer could appear in many rows. The same student could appear in many rows. One application could also need several rows if it has more than one interview. This can lead to update, insertion, and deletion problems.

## Main Functional Dependencies

These are the main functional dependencies we think should hold:

- `student_id -> full_name, username, email, program`
- `employer_id -> employer_name, industry, website, city, province, country`
- `posting_id -> employer_id, job_title, work_term, location_type, city, province, country, posting_url, date_posted, application_deadline, salary_range, posting_status`
- `status_id -> status_name, is_terminal`
- `resume_id -> student_id, resume_label, version_number, created_on, file_name`
- `application_id -> student_id, posting_id, status_id, resume_id, date_applied, source, priority, notes`
- `interview_id -> application_id, interview_round, interview_type, scheduled_at, location, interviewer_name, result`
- `offer_id -> application_id, hourly_wage, offer_date, response_deadline, offer_status, notes`

There are also some alternate uniqueness rules:

- `username -> student_id`
- `status_name -> status_id`
- `posting_url -> posting_id` when a posting URL is provided
- `(student_id, posting_id) -> application_id`
- `(application_id, interview_round) -> interview_id`
- `application_id -> offer_id` for offers, because we are allowing at most one offer per application

## Keys And BCNF

In our design, each table has a primary key, and the other attributes depend on that key. For example, in `Employer`, the employer name, industry, website, and location all depend on `employer_id`.

For BCNF, the main idea we used is that every non-trivial functional dependency should have a superkey on the left side. The design is close to BCNF because facts are separated into their own tables:

- employer facts are only in `Employer`
- job posting facts are only in `JobPosting`
- student facts are only in `Student`
- status facts are only in `ApplicationStatus`
- interview facts are only in `Interview`
- offer facts are only in `Offer`

Acc to us, this avoids the main anomaly problem from putting everything in one relation. For example, deleting a rejected application will not delete the employer from the database. Also, changing an employer website does not require updating every application row.

## Small BCNF Example From Our Design

Suppose we had this relation:

`ApplicationFlat(application_id, student_id, student_name, posting_id, employer_name, status_name)`

Some FDs would be:

- `application_id -> student_id, posting_id, status_name`
- `student_id -> student_name`
- `posting_id -> employer_name`

This is not in BCNF because `student_id` determines `student_name`, but `student_id` is not a superkey for the whole relation. Also, `posting_id` determines `employer_name`, but `posting_id` is not a superkey for the whole relation.

So we decomposed it into separate relations like:

- `Student(student_id, full_name, username, email, program)`
- `JobPosting(posting_id, employer_id, job_title, ...)`
- `Employer(employer_id, employer_name, ...)`
- `Application(application_id, student_id, posting_id, status_id, ...)`
- `ApplicationStatus(status_id, status_name, is_terminal)`

This is why the schema has more tables, even though it may look longer.
