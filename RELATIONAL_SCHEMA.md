# Relational schema - Sprint 1

Reference for `schema.sql`. All attributes are shown. Optional means SQL NULL is allowed.

## Student

| Attribute | SQL type | Optional |
| --- | --- | --- |
| student_id | INT | no |
| full_name | VARCHAR(100) | no |
| username | VARCHAR(40) | no |
| email | VARCHAR(120) | yes |
| program | VARCHAR(80) | yes |

Primary key: `student_id`.
Non-null candidate keys: `student_id`; `username`.

SQL UNIQUE: `username`.

SQL UNIQUE: `email` (nullable: not an unconditional classical candidate key).

## Employer

| Attribute | SQL type | Optional |
| --- | --- | --- |
| employer_id | INT | no |
| employer_name | VARCHAR(120) | no |
| industry | VARCHAR(80) | yes |
| website | VARCHAR(200) | yes |
| city | VARCHAR(80) | yes |
| province | VARCHAR(40) | yes |
| country | VARCHAR(60) | yes |

Primary key: `employer_id`.
Non-null candidate keys: `employer_id`.

SQL UNIQUE: `employer_name, website` (nullable: not an unconditional classical candidate key).

## JobPosting

| Attribute | SQL type | Optional |
| --- | --- | --- |
| posting_id | INT | no |
| employer_id | INT | no |
| job_title | VARCHAR(120) | no |
| work_term | VARCHAR(40) | no |
| location_type | ENUM('remote', 'in_person', 'hybrid') | no |
| city | VARCHAR(80) | yes |
| province | VARCHAR(40) | yes |
| country | VARCHAR(60) | yes |
| posting_url | VARCHAR(500) | yes |
| date_posted | DATE | yes |
| application_deadline | DATE | yes |
| salary_range | VARCHAR(80) | yes |
| posting_status | ENUM('open', 'closed', 'cancelled') | no |

Primary key: `posting_id`.
Non-null candidate keys: `posting_id`.

SQL UNIQUE: `posting_url` (nullable: not an unconditional classical candidate key).

Foreign key: `employer_id` -> `Employer.employer_id` (default RESTRICT/NO ACTION).

## ApplicationStatus

| Attribute | SQL type | Optional |
| --- | --- | --- |
| status_id | INT | no |
| status_name | VARCHAR(40) | no |
| is_terminal | BOOLEAN | no |

Primary key: `status_id`.
Non-null candidate keys: `status_id`; `status_name`.

SQL UNIQUE: `status_name`.

## ResumeVersion

| Attribute | SQL type | Optional |
| --- | --- | --- |
| resume_id | INT | no |
| student_id | INT | no |
| resume_label | VARCHAR(80) | no |
| version_number | INT | no |
| created_on | DATE | no |
| file_name | VARCHAR(200) | yes |

Primary key: `resume_id`.
Non-null candidate keys: `resume_id`; `student_id, version_number`.

SQL UNIQUE: `student_id, version_number`.

Foreign key: `student_id` -> `Student.student_id` (default RESTRICT/NO ACTION).

## Application

| Attribute | SQL type | Optional |
| --- | --- | --- |
| application_id | INT | no |
| student_id | INT | no |
| posting_id | INT | no |
| status_id | INT | no |
| date_applied | DATE | yes |
| source | VARCHAR(80) | yes |
| priority | INT | no |
| notes | TEXT | yes |

Primary key: `application_id`.
Non-null candidate keys: `application_id`; `student_id, posting_id`.

SQL UNIQUE: `student_id, posting_id`.

Foreign key: `student_id` -> `Student.student_id` (default RESTRICT/NO ACTION).

Foreign key: `posting_id` -> `JobPosting.posting_id` (default RESTRICT/NO ACTION).

Foreign key: `status_id` -> `ApplicationStatus.status_id` (default RESTRICT/NO ACTION).

## Interview

| Attribute | SQL type | Optional |
| --- | --- | --- |
| interview_id | INT | no |
| application_id | INT | no |
| interview_round | INT | no |
| interview_type | ENUM('phone', 'video', 'in_person', 'technical', 'hr') | no |
| scheduled_at | DATETIME | no |
| location | VARCHAR(200) | yes |
| interviewer_name | VARCHAR(120) | yes |
| result | ENUM('scheduled', 'passed', 'failed', 'cancelled', 'unknown') | no |

Primary key: `interview_id`.
Non-null candidate keys: `interview_id`; `application_id, interview_round`.

SQL UNIQUE: `application_id, interview_round`.

Foreign key: `application_id` -> `Application.application_id` (default RESTRICT/NO ACTION).

## Offer

| Attribute | SQL type | Optional |
| --- | --- | --- |
| offer_id | INT | no |
| application_id | INT | no |
| hourly_wage | DECIMAL(6,2) | yes |
| offer_date | DATE | no |
| response_deadline | DATE | yes |
| offer_status | ENUM('pending', 'accepted', 'declined', 'expired') | no |
| notes | TEXT | yes |

Primary key: `offer_id`.
Non-null candidate keys: `offer_id`; `application_id`.

SQL UNIQUE: `application_id`.

Foreign key: `application_id` -> `Application.application_id` (default RESTRICT/NO ACTION).

## ApplicationResume

| Attribute | SQL type | Optional |
| --- | --- | --- |
| application_id | INT | no |
| resume_id | INT | no |

Primary key: `application_id`.
Non-null candidate keys: `application_id`.

Foreign key: `application_id` -> `Application.application_id` (default RESTRICT/NO ACTION).

Foreign key: `resume_id` -> `ResumeVersion.resume_id` (default RESTRICT/NO ACTION).
