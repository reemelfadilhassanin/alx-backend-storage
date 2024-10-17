-- 101-average_weighted_score.sql

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score and total weight for the current user
        SELECT 
            SUM(c.score * p.weight) INTO total_score,
            SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Update the average_score in the users table
        IF total_weight > 0 THEN
            UPDATE users 
            SET average_score = total_score / total_weight 
            WHERE id = user_id;
        ELSE
            UPDATE users 
            SET average_score = 0 
            WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;
