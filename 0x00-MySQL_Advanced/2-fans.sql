-- This script ranks country origins of bands, ordered by the number of non-unique fans

SELECT 
    origin, 
    COUNT(*) AS nb_fans
FROM 
    bands  -- Replace 'bands' with the actual table name if different
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
