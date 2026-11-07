USE coop_application_tracker_sprint1;

-- name: O1
-- A current-status funnel summary, not historical stage conversion rates.
WITH status_counts AS (
    SELECT st.status_id, st.status_name, COUNT(a.application_id) AS n
    FROM ApplicationStatus AS st
    LEFT JOIN Application AS a ON a.status_id = st.status_id
    GROUP BY st.status_id, st.status_name
), total AS (
    SELECT COUNT(*) AS n FROM Application
)
SELECT sc.status_id, sc.status_name, sc.n,
       COALESCE(ROUND(100.0 * sc.n / NULLIF(total.n, 0), 2), 0.00) AS percent_of_applications
FROM status_counts AS sc
CROSS JOIN total
ORDER BY sc.status_id;

-- name: O2
-- Posting/application IDs make equal-priority ordering deterministic.
SELECT student_id, application_id, priority,
       ROW_NUMBER() OVER (
           PARTITION BY student_id ORDER BY priority, posting_id, application_id
       ) AS priority_rank
FROM Application
ORDER BY student_id, priority_rank;
