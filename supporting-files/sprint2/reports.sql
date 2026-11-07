USE coop_application_tracker_sprint1;

-- name: R1
-- Every student's workload, including students with no applications.
SELECT student_id, full_name, application_count, active_application_count,
       interviewed_application_count, offered_application_count
FROM StudentWorkload
ORDER BY student_id;

-- name: R2
-- Employers with at least two tracked applications; WHERE filters postings before grouping.
SELECT e.employer_id, e.employer_name, COUNT(a.application_id) AS application_count
FROM Employer AS e
JOIN JobPosting AS p ON p.employer_id = e.employer_id
JOIN Application AS a ON a.posting_id = p.posting_id
WHERE p.work_term = 'Spring 2027'
GROUP BY e.employer_id, e.employer_name
HAVING COUNT(a.application_id) >= 2
ORDER BY e.employer_id;

-- name: R3
-- Numerically higher priority values mean less urgent applications in this tracker.
SELECT a.application_id, a.student_id, a.priority
FROM Application AS a
WHERE a.priority > (
    SELECT AVG(other.priority)
    FROM Application AS other
    WHERE other.student_id = a.student_id
)
ORDER BY a.application_id;

-- name: R4
-- Students with no interview on any of their applications (including no applications).
SELECT s.student_id, s.full_name
FROM Student AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM Application AS a
    JOIN Interview AS i ON i.application_id = a.application_id
    WHERE a.student_id = s.student_id
)
ORDER BY s.student_id;

-- name: R5
-- Missing selection is a missing relationship, not a NULL resume_id in that relationship.
SELECT a.application_id, a.student_id
FROM Application AS a
LEFT JOIN ApplicationResume AS ar ON ar.application_id = a.application_id
WHERE ar.application_id IS NULL
ORDER BY a.application_id;

-- name: R6
-- Students who need a resume selection or have no applications; UNION removes repeats.
SELECT a.student_id
FROM Application AS a
WHERE NOT EXISTS (
    SELECT 1 FROM ApplicationResume AS ar WHERE ar.application_id = a.application_id
)
UNION
SELECT s.student_id
FROM Student AS s
WHERE NOT EXISTS (
    SELECT 1 FROM Application AS a WHERE a.student_id = s.student_id
)
ORDER BY student_id;

-- name: R7
-- All status labels, including unused ones. COUNT(*) would overcount an unmatched label.
SELECT st.status_id, st.status_name, COUNT(a.application_id) AS application_count
FROM ApplicationStatus AS st
LEFT JOIN Application AS a ON a.status_id = st.status_id
GROUP BY st.status_id, st.status_name
ORDER BY st.status_id;

-- name: R8
-- Relational division: actually applied to every open posting (saved-only rows do not count).
-- If there are no open postings, every student satisfies the condition.
SELECT s.student_id, s.full_name
FROM Student AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM JobPosting AS p
    WHERE p.posting_status = 'open'
      AND NOT EXISTS (
          SELECT 1 FROM Application AS a
          WHERE a.student_id = s.student_id AND a.posting_id = p.posting_id
            AND a.date_applied IS NOT NULL
      )
)
ORDER BY s.student_id;
