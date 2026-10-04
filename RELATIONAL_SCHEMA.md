# Relational Schema

This is the relational version of the ERD. Primary keys are marked with `PK`, and foreign keys are marked with `FK`.

## Tables

`Student(student_id PK, full_name, username, email, program)`

- `username` should be unique.
- `email` should be unique when it is provided.

`Employer(employer_id PK, employer_name, industry, website, city, province, country)`

- `employer_name` and `website` together should be unique.

`JobPosting(posting_id PK, employer_id FK, job_title, work_term, location_type, city, province, country, posting_url, date_posted, application_deadline, salary_range, posting_status)`

- `employer_id` references `Employer(employer_id)`.
- `posting_url` should be unique when it is provided.

`ApplicationStatus(status_id PK, status_name, is_terminal)`

- `status_name` should be unique.

`ResumeVersion(resume_id PK, student_id FK, resume_label, version_number, created_on, file_name)`

- `student_id` references `Student(student_id)`.
- `(student_id, version_number)` should be unique.

`Application(application_id PK, student_id FK, posting_id FK, status_id FK, resume_id FK, date_applied, source, priority, notes)`

- `student_id` references `Student(student_id)`.
- `posting_id` references `JobPosting(posting_id)`.
- `status_id` references `ApplicationStatus(status_id)`.
- `resume_id` references `ResumeVersion(resume_id)`.
- `(student_id, posting_id)` should be unique so the same student does not apply twice to the same posting.

`Interview(interview_id PK, application_id FK, interview_round, interview_type, scheduled_at, location, interviewer_name, result)`

- `application_id` references `Application(application_id)`.
- `(application_id, interview_round)` should be unique.

`Offer(offer_id PK, application_id FK, hourly_wage, offer_date, response_deadline, offer_status, notes)`

- `application_id` references `Application(application_id)`.
- `application_id` is unique so one application has at most one offer in this first version.

## Why These Tables Are Split

We split the database this way to avoid repeating the same facts many times. For example, employer details are stored once in `Employer`, not copied into every application. Application status names are also stored in `ApplicationStatus`, so we do not have to repeat the exact same words everywhere.

This also makes the database easier to update. If an employer website changes, we update one row instead of many rows.
