-- 100-average_weighted_score.sql
BEGIN
	UPDATE users SET average_score = (SELECT
	SUM(corrections.score * projects.weight) / SUM(projects.weight)
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id)
	WHERE users.id = user_id;
END $$
DELIMITER ;
