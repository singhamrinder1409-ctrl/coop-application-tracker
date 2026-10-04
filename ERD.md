# ERD

## Rendered Diagram

![Co-op Application Tracker ERD](ERD.svg)

## Conceptual Design

The main idea is to describe what should be in the database before thinking too much about screens or code. For this project, the important things are students, employers, job postings, applications, statuses, resume versions, interviews, and offers.

We chose these entity sets because each one has its own information and its own identifier. For example, an employer has a name and website, while a job posting has a title, deadline, and work term. We think those should be separate because one employer can have many postings.

## Entity Sets And Identifiers

| Entity Set | Identifier | Notes |
| --- | --- | --- |
| Student | `student_id` | A student using the tracker |
| Employer | `employer_id` | A company or organization |
| JobPosting | `posting_id` | A job posted by an employer |
| ApplicationStatus | `status_id` | Lookup table for statuses |
| ResumeVersion | `resume_id` | A resume version owned by a student |
| Application | `application_id` | A student's application to a posting |
| Interview | `interview_id` | One interview round for an application |
| Offer | `offer_id` | An offer for an application |

## Main Relationships And Multiplicities

- One employer can create many job postings.
- Each job posting belongs to exactly one employer.
- One student can have many resume versions.
- One student can submit many applications.
- One job posting can have many applications.
- Each application belongs to one student and one job posting.
- Each application has one current status.
- One application can have many interviews.
- One application can have zero or one offer in this first design.

## Mermaid ERD

This diagram uses crow's foot notation because it works well in GitHub. The course uses a Chen-style ERD in class, but the same main ideas are here: entity sets, attributes, identifiers, relationships, and multiplicities.

```mermaid
erDiagram
    STUDENT ||--o{ RESUME_VERSION : owns
    STUDENT ||--o{ APPLICATION : submits
    EMPLOYER ||--o{ JOB_POSTING : posts
    JOB_POSTING ||--o{ APPLICATION : receives
    APPLICATION_STATUS ||--o{ APPLICATION : labels
    RESUME_VERSION ||--o{ APPLICATION : used_for
    APPLICATION ||--o{ INTERVIEW : has
    APPLICATION ||--o| OFFER : may_receive

    STUDENT {
        int student_id PK
        varchar full_name
        varchar username
        varchar email
        varchar program
    }

    EMPLOYER {
        int employer_id PK
        varchar employer_name
        varchar industry
        varchar website
        varchar city
        varchar province
        varchar country
    }

    JOB_POSTING {
        int posting_id PK
        int employer_id FK
        varchar job_title
        varchar work_term
        varchar location_type
        varchar city
        varchar province
        varchar country
        varchar posting_url
        date date_posted
        date application_deadline
        varchar salary_range
        varchar posting_status
    }

    APPLICATION_STATUS {
        int status_id PK
        varchar status_name
        boolean is_terminal
    }

    RESUME_VERSION {
        int resume_id PK
        int student_id FK
        varchar resume_label
        int version_number
        date created_on
        varchar file_name
    }

    APPLICATION {
        int application_id PK
        int student_id FK
        int posting_id FK
        int status_id FK
        int resume_id FK
        date date_applied
        varchar source
        int priority
        text notes
    }

    INTERVIEW {
        int interview_id PK
        int application_id FK
        int interview_round
        varchar interview_type
        datetime scheduled_at
        varchar location
        varchar interviewer_name
        varchar result
    }

    OFFER {
        int offer_id PK
        int application_id FK
        decimal hourly_wage
        date offer_date
        date response_deadline
        varchar offer_status
        text notes
    }
```
