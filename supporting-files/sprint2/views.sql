USE coop_application_tracker_sprint1;

-- Count children before joining, so two interviews do not duplicate an offer.
CREATE OR REPLACE SQL SECURITY INVOKER VIEW ApplicationOverview
    (application_id, student_id, full_name, posting_id, job_title,
     employer_id, employer_name, status_name, is_terminal, priority,
     resume_id, interview_count, offer_id) AS
SELECT a.application_id, a.student_id, s.full_name, a.posting_id, p.job_title,
       e.employer_id, e.employer_name, st.status_name, st.is_terminal, a.priority,
       ar.resume_id, COALESCE(i.interview_count, 0), o.offer_id
FROM Application AS a
JOIN Student AS s ON s.student_id = a.student_id
JOIN JobPosting AS p ON p.posting_id = a.posting_id
JOIN Employer AS e ON e.employer_id = p.employer_id
JOIN ApplicationStatus AS st ON st.status_id = a.status_id
LEFT JOIN ApplicationResume AS ar ON ar.application_id = a.application_id
LEFT JOIN (
    SELECT application_id, COUNT(*) AS interview_count
    FROM Interview
    GROUP BY application_id
) AS i ON i.application_id = a.application_id
LEFT JOIN Offer AS o ON o.application_id = a.application_id;

CREATE OR REPLACE SQL SECURITY INVOKER VIEW StudentWorkload
    (student_id, full_name, application_count, active_application_count,
     interviewed_application_count, offered_application_count) AS
SELECT s.student_id, s.full_name, COUNT(a.application_id),
       SUM(CASE WHEN a.is_terminal = 0 THEN 1 ELSE 0 END),
       SUM(CASE WHEN a.interview_count > 0 THEN 1 ELSE 0 END),
       COUNT(a.offer_id)
FROM Student AS s
LEFT JOIN ApplicationOverview AS a ON a.student_id = s.student_id
GROUP BY s.student_id, s.full_name;
