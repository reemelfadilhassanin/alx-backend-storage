-- 9-index_name_score.sql

DROP INDEX IF EXISTS idx_name_first_score ON names;

CREATE INDEX idx_name_first_score ON names (name(1), score);
