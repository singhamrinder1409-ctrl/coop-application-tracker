USE coop_application_tracker_sprint1;

-- name: E1A
SELECT a.application_id
FROM Application AS a
WHERE NOT EXISTS (
    SELECT 1 FROM ApplicationResume AS ar WHERE ar.application_id = a.application_id
)
ORDER BY a.application_id;
-- name: E1B
SELECT a.application_id
FROM Application AS a
LEFT JOIN ApplicationResume AS ar ON ar.application_id = a.application_id
WHERE ar.application_id IS NULL
ORDER BY a.application_id;

-- name: E2A
SELECT s.student_id,
       (SELECT COUNT(*) FROM Application AS a WHERE a.student_id = s.student_id) AS n
FROM Student AS s
ORDER BY s.student_id;
-- name: E2B
SELECT s.student_id, COALESCE(c.n, 0) AS n
FROM Student AS s
LEFT JOIN (
    SELECT student_id, COUNT(*) AS n FROM Application GROUP BY student_id
) AS c ON c.student_id = s.student_id
ORDER BY s.student_id;

-- name: E3A
SELECT a.application_id
FROM Application AS a
WHERE EXISTS (SELECT 1 FROM Interview AS i WHERE i.application_id = a.application_id)
ORDER BY a.application_id;
-- name: E3B
SELECT DISTINCT a.application_id
FROM Application AS a
JOIN Interview AS i ON i.application_id = a.application_id
ORDER BY a.application_id;

-- name: E4A
SELECT application_id FROM Application WHERE priority <= 2
UNION
SELECT application_id FROM Application WHERE source IS NULL
ORDER BY application_id;
-- name: E4B
SELECT application_id FROM Application
WHERE priority <= 2 OR source IS NULL
ORDER BY application_id;
