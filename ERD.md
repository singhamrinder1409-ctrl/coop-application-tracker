# Complete ERD - Sprint 1

Crow's-foot notation replaces the incomplete kick-off Chen diagram. Every SQL attribute appears below and in `ERD.svg`; the Mermaid source and relational schema also show SQL types. `PK` is the primary key, `FK` a reference, and `UK` a non-null alternate key component. See `RELATIONAL_SCHEMA.md` for nullable UNIQUE rules.

```mermaid
erDiagram
    Student {
        INT student_id PK
        VARCHAR_100_ full_name
        VARCHAR_40_ username UK
        VARCHAR_120_ email
        VARCHAR_80_ program
    }
    Employer {
        INT employer_id PK
        VARCHAR_120_ employer_name
        VARCHAR_80_ industry
        VARCHAR_200_ website
        VARCHAR_80_ city
        VARCHAR_40_ province
        VARCHAR_60_ country
    }
    JobPosting {
        INT posting_id PK
        INT employer_id FK
        VARCHAR_120_ job_title
        VARCHAR_40_ work_term
        ENUM__remote____in_person____hybrid__ location_type
        VARCHAR_80_ city
        VARCHAR_40_ province
        VARCHAR_60_ country
        VARCHAR_500_ posting_url
        DATE date_posted
        DATE application_deadline
        VARCHAR_80_ salary_range
        ENUM__open____closed____cancelled__ posting_status
    }
    ApplicationStatus {
        INT status_id PK
        VARCHAR_40_ status_name UK
        BOOLEAN is_terminal
    }
    ResumeVersion {
        INT resume_id PK
        INT student_id FK,UK
        VARCHAR_80_ resume_label
        INT version_number UK
        DATE created_on
        VARCHAR_200_ file_name
    }
    Application {
        INT application_id PK
        INT student_id FK,UK
        INT posting_id FK,UK
        INT status_id FK
        DATE date_applied
        VARCHAR_80_ source
        INT priority
        TEXT notes
    }
    Interview {
        INT interview_id PK
        INT application_id FK,UK
        INT interview_round UK
        ENUM__phone____video____in_person____technical____hr__ interview_type
        DATETIME scheduled_at
        VARCHAR_200_ location
        VARCHAR_120_ interviewer_name
        ENUM__scheduled____passed____failed____cancelled____unknown__ result
    }
    Offer {
        INT offer_id PK
        INT application_id FK,UK
        DECIMAL_6_2_ hourly_wage
        DATE offer_date
        DATE response_deadline
        ENUM__pending____accepted____declined____expired__ offer_status
        TEXT notes
    }
    ApplicationResume {
        INT application_id PK,FK
        INT resume_id FK
    }
    Employer ||--o{ JobPosting : posts
    Student ||--o{ ResumeVersion : owns
    Student ||--o{ Application : submits
    JobPosting ||--o{ Application : receives
    ApplicationStatus ||--o{ Application : classifies
    Application ||--o{ Interview : has
    Application ||--o| Offer : receives
    Application ||--o| ApplicationResume : selects
    ResumeVersion ||--o{ ApplicationResume : used_by
```

Every child has exactly one parent for each listed reference; each parent has zero or many children, except Offer and ApplicationResume (zero or one). An application without ApplicationResume has no selected resume. Ownership consistency also requires the triggers described in `docs/CONSTRAINTS.md`.

![Complete ERD](ERD.svg)
