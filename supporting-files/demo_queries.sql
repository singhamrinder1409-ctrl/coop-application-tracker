USE coop_application_tracker_sprint1;

-- 1. All applications with their current status.
SELECT
    s.full_name,
    e.employer_name,
    jp.job_title,
    a.date_applied,
    ast.status_name,
    a.priority
FROM Application AS a
JOIN Student AS s
    ON s.student_id = a.student_id
JOIN JobPosting AS jp
    ON jp.posting_id = a.posting_id
JOIN Employer AS e
    ON e.employer_id = jp.employer_id
JOIN ApplicationStatus AS ast
    ON ast.status_id = a.status_id
ORDER BY a.priority, a.date_applied;

-- 2. Applications that are still active.
SELECT
    s.full_name,
    e.employer_name,
    jp.job_title,
    ast.status_name
FROM Application AS a
JOIN Student AS s
    ON s.student_id = a.student_id
JOIN JobPosting AS jp
    ON jp.posting_id = a.posting_id
JOIN Employer AS e
    ON e.employer_id = jp.employer_id
JOIN ApplicationStatus AS ast
    ON ast.status_id = a.status_id
WHERE ast.is_terminal = FALSE;

-- 3. Upcoming interviews.
SELECT
    s.full_name,
    e.employer_name,
    jp.job_title,
    i.interview_round,
    i.interview_type,
    i.scheduled_at,
    i.location
FROM Interview AS i
JOIN Application AS a
    ON a.application_id = i.application_id
JOIN Student AS s
    ON s.student_id = a.student_id
JOIN JobPosting AS jp
    ON jp.posting_id = a.posting_id
JOIN Employer AS e
    ON e.employer_id = jp.employer_id
-- Fixed as-of date makes the recording and automated assertions repeatable.
WHERE i.result = 'scheduled' AND i.scheduled_at >= '2026-10-18 00:00:00'
ORDER BY i.scheduled_at;

-- 4. Number of applications in each status.
SELECT
    ast.status_name,
    COUNT(*) AS application_count
FROM Application AS a
JOIN ApplicationStatus AS ast
    ON ast.status_id = a.status_id
GROUP BY ast.status_name
ORDER BY application_count DESC, ast.status_name;

-- 5. Offers and response deadlines.
SELECT
    s.full_name,
    e.employer_name,
    jp.job_title,
    o.hourly_wage,
    o.offer_date,
    o.response_deadline,
    o.offer_status
FROM Offer AS o
JOIN Application AS a
    ON a.application_id = o.application_id
JOIN Student AS s
    ON s.student_id = a.student_id
JOIN JobPosting AS jp
    ON jp.posting_id = a.posting_id
JOIN Employer AS e
    ON e.employer_id = jp.employer_id;

-- 6. Application workload for every student, including students with no applications.
-- COUNT(application_id), rather than COUNT(*), makes the unmatched student count 0.
SELECT s.full_name, COUNT(a.application_id) AS application_count
FROM Student AS s
LEFT JOIN Application AS a ON a.student_id = s.student_id
GROUP BY s.student_id, s.full_name
ORDER BY s.student_id;

-- 7. Applications with no resume selected (a missing relationship, not an orphan FK).
SELECT a.application_id, s.full_name, jp.job_title
FROM Application AS a
JOIN Student AS s ON s.student_id = a.student_id
JOIN JobPosting AS jp ON jp.posting_id = a.posting_id
LEFT JOIN ApplicationResume AS ar ON ar.application_id = a.application_id
WHERE ar.application_id IS NULL
ORDER BY a.application_id;
