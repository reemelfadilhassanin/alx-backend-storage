-- 8-index_my_names.sql

DROP INDEX IF EXISTS idx_name_first ON names;

CREATE INDEX idx_name_first ON names (name(1));
