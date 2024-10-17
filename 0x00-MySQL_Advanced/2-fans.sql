-- This script ranks country origins of bands, ordered by the number of non-unique fansSELECT     origin,     COUNT(*) AS nb_fansFROM     bands  -- Replace 'bands' with the actual table name if differentGROUP BY     originORDER BY     nb_fans DESC;
SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
