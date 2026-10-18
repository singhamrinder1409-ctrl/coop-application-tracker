DROP DATABASE IF EXISTS coop_application_tracker;
CREATE DATABASE coop_application_tracker;
USE coop_application_tracker;

CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(120),
    program VARCHAR(80),
    UNIQUE (username),
    UNIQUE (email)
);

CREATE TABLE Employer (
    employer_id INT AUTO_INCREMENT PRIMARY KEY,
    employer_name VARCHAR(120) NOT NULL,
    industry VARCHAR(80),
    website VARCHAR(200),
    city VARCHAR(80),
    province VARCHAR(40),
    country VARCHAR(60) DEFAULT 'Canada',
    UNIQUE (employer_name, website)
);

CREATE TABLE JobPosting (
    posting_id INT AUTO_INCREMENT PRIMARY KEY,
    employer_id INT NOT NULL,
    job_title VARCHAR(120) NOT NULL,
    work_term VARCHAR(40) NOT NULL,
    location_type ENUM('remote', 'in_person', 'hybrid') NOT NULL DEFAULT 'in_person',
    city VARCHAR(80),
    province VARCHAR(40),
    country VARCHAR(60) DEFAULT 'Canada',
    posting_url VARCHAR(500),
    date_posted DATE,
    application_deadline DATE,
    salary_range VARCHAR(80),
    posting_status ENUM('open', 'closed', 'cancelled') NOT NULL DEFAULT 'open',
    FOREIGN KEY (employer_id) REFERENCES Employer(employer_id),
    UNIQUE (posting_url),
    CHECK (application_deadline IS NULL OR date_posted IS NULL OR application_deadline >= date_posted)
);

CREATE TABLE ApplicationStatus (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(40) NOT NULL,
    is_terminal BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (status_name)
);

CREATE TABLE ResumeVersion (
    resume_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    resume_label VARCHAR(80) NOT NULL,
    version_number INT NOT NULL,
    created_on DATE NOT NULL,
    file_name VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    UNIQUE (student_id, version_number),
    CHECK (version_number > 0)
);

CREATE TABLE Application (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    posting_id INT NOT NULL,
    status_id INT NOT NULL,
    resume_id INT,
    date_applied DATE,
    source VARCHAR(80),
    priority INT DEFAULT 3,
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (posting_id) REFERENCES JobPosting(posting_id),
    FOREIGN KEY (status_id) REFERENCES ApplicationStatus(status_id),
    FOREIGN KEY (resume_id) REFERENCES ResumeVersion(resume_id),
    UNIQUE (student_id, posting_id),
    CHECK (priority BETWEEN 1 AND 5)
);

CREATE TABLE Interview (
    interview_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    interview_round INT NOT NULL,
    interview_type ENUM('phone', 'video', 'in_person', 'technical', 'hr') NOT NULL,
    scheduled_at DATETIME NOT NULL,
    location VARCHAR(200),
    interviewer_name VARCHAR(120),
    result ENUM('scheduled', 'passed', 'failed', 'cancelled', 'unknown') NOT NULL DEFAULT 'scheduled',
    FOREIGN KEY (application_id) REFERENCES Application(application_id),
    UNIQUE (application_id, interview_round),
    CHECK (interview_round > 0)
);

CREATE TABLE Offer (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    hourly_wage DECIMAL(6,2),
    offer_date DATE NOT NULL,
    response_deadline DATE,
    offer_status ENUM('pending', 'accepted', 'declined', 'expired') NOT NULL DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (application_id) REFERENCES Application(application_id),
    UNIQUE (application_id),
    CHECK (hourly_wage IS NULL OR hourly_wage >= 0),
    CHECK (response_deadline IS NULL OR response_deadline >= offer_date)
);

