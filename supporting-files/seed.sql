USE coop_application_tracker_sprint1;

INSERT INTO Student (full_name, username, email, program)
VALUES
    ('Amrinder Singh', 'amrinder', NULL, 'Computer Science'),
    ('Jaiman Singh', 'jaiman1', NULL, 'Computer Science'),
    ('Aashna Sadeque', 'aashnas', NULL, 'Computer Science');

INSERT INTO Employer (employer_name, industry, website, city, province, country)
VALUES
    ('Ocean Analytics Lab', 'Research', 'https://example.com/ocean-analytics', 'Victoria', 'BC', 'Canada'),
    ('Northwind Software', 'Software', 'https://example.com/northwind', 'Vancouver', 'BC', 'Canada'),
    ('Island Health Data Team', 'Healthcare', 'https://example.com/island-health-data', 'Victoria', 'BC', 'Canada');

INSERT INTO JobPosting (
    employer_id, job_title, work_term, location_type, city, province, country,
    posting_url, date_posted, application_deadline, salary_range, posting_status
)
VALUES
    (1, 'Data Systems Co-op', 'Spring 2027', 'hybrid', 'Victoria', 'BC', 'Canada',
     'https://example.com/jobs/ocean-data-systems', '2026-10-01', '2026-10-20', '$25-$30/hour', 'open'),
    (2, 'Backend Developer Co-op', 'Spring 2027', 'remote', 'Vancouver', 'BC', 'Canada',
     'https://example.com/jobs/northwind-backend', '2026-10-02', '2026-10-24', '$28-$34/hour', 'open'),
    (3, 'Health Data Analyst Co-op', 'Spring 2027', 'in_person', 'Victoria', 'BC', 'Canada',
     'https://example.com/jobs/health-data-analyst', '2026-09-28', '2026-10-15', '$24-$29/hour', 'closed');

INSERT INTO ApplicationStatus (status_name, is_terminal)
VALUES
    ('saved', FALSE),
    ('applied', FALSE),
    ('interview', FALSE),
    ('offer', FALSE),
    ('rejected', TRUE),
    ('withdrawn', TRUE);

INSERT INTO ResumeVersion (student_id, resume_label, version_number, created_on, file_name)
VALUES
    (1, 'Data focused resume', 1, '2026-09-25', 'amrinder_resume_data_v1.pdf'),
    (1, 'Backend focused resume', 2, '2026-09-30', 'amrinder_resume_backend_v2.pdf'),
    (2, 'General software resume', 1, '2026-09-26', 'jaiman_resume_v1.pdf'),
    (3, 'Data analyst resume', 1, '2026-09-26', 'aashna_resume_data_v1.pdf');

INSERT INTO Application (student_id, posting_id, status_id, date_applied, source, priority, notes)
VALUES
    (1, 1, 3, '2026-10-04', 'UVic Co-op Portal', 1, 'Interview booked. Review SQL notes.'),
    (1, 2, 2, '2026-10-04', 'Company Website', 2, 'Backend role looks interesting.'),
    (2, 2, 1, NULL, 'UVic Co-op Portal', 3, 'Saved but not applied yet.'),
    (3, 3, 4, '2026-10-01', 'UVic Co-op Portal', 4, 'Sample application with an offer.');

INSERT INTO Interview (application_id, interview_round, interview_type, scheduled_at, location, interviewer_name, result)
VALUES
    (1, 1, 'video', '2026-10-12 10:30:00', 'Zoom', 'Taylor Chen', 'scheduled');

INSERT INTO Offer (application_id, hourly_wage, offer_date, response_deadline, offer_status, notes)
VALUES
    (4, 28.50, '2026-10-18', '2026-10-25', 'pending', 'Sample offer row for demo only.');

INSERT INTO ApplicationResume VALUES (1, 1), (2, 2), (3, 3), (4, 4);
-- Edge cases: no applications, no resume selected, multiple interview rounds,
-- NULL unique values, zero wage, and a rejected application.
INSERT INTO Student VALUES (4, 'Demo Student', 'demo_student', NULL, 'Computer Science');
INSERT INTO Application (student_id, posting_id, status_id, priority)
VALUES (2, 1, 5, 5), (3, 2, 1, 3);
INSERT INTO Interview (application_id, interview_round, interview_type, scheduled_at, result)
VALUES (1, 2, 'technical', '2026-10-21 14:00:00', 'scheduled');
INSERT INTO Offer (application_id, hourly_wage, offer_date, response_deadline)
VALUES (2, 0.00, '2026-10-18', '2026-10-18');
