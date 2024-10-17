-- 100-average_weighted_score.sql

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    -- Calculate the total weighted score and total weight
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
END //

DELIMITER ;
