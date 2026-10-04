USE coop_application_tracker;

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
WHERE i.result = 'scheduled'
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
