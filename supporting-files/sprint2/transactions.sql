USE coop_application_tracker_sprint1;

-- Standalone operation: call on a fresh connection, outside any caller transaction.
-- START TRANSACTION would otherwise implicitly commit an already open transaction.
-- Error handling pattern: https://dev.mysql.com/doc/refman/8.4/en/resignal.html
DROP PROCEDURE IF EXISTS ScheduleInterview;
DELIMITER $$
CREATE PROCEDURE ScheduleInterview(
    IN p_application_id INT,
    IN p_round INT,
    IN p_type VARCHAR(20),
    IN p_scheduled_at DATETIME
)
SQL SECURITY INVOKER
BEGIN
    IF @@autocommit <> 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Use a standalone autocommit connection';
    END IF;
    BEGIN
        DECLARE v_application_id INT DEFAULT NULL;
        DECLARE v_terminal BOOLEAN DEFAULT NULL;
        DECLARE v_interview_status INT DEFAULT NULL;
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

        START TRANSACTION;
        SELECT a.application_id, st.is_terminal
        INTO v_application_id, v_terminal
        FROM Application AS a
        JOIN ApplicationStatus AS st ON st.status_id = a.status_id
        WHERE a.application_id = p_application_id
        FOR UPDATE;
        IF v_application_id IS NULL THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Application does not exist';
        END IF;
        IF v_terminal THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot schedule a terminal application';
        END IF;
        IF p_type IS NULL OR p_type NOT IN ('phone', 'video', 'in_person', 'technical', 'hr') THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid interview type';
        END IF;
        SELECT status_id INTO v_interview_status
        FROM ApplicationStatus
        WHERE status_name = 'interview' AND is_terminal = 0;
        IF v_interview_status IS NULL THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Interview status is missing or terminal';
        END IF;

        UPDATE Application SET status_id = v_interview_status
        WHERE application_id = p_application_id;
        INSERT INTO Interview(application_id, interview_round, interview_type, scheduled_at)
        VALUES(p_application_id, p_round, p_type, p_scheduled_at);
        COMMIT;
    END;
END$$
DELIMITER ;
