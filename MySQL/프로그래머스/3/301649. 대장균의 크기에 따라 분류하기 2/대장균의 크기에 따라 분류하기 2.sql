# 백분위로 순서를 부여
WITH A
    AS (SELECT 
            *, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PCT
        FROM 
            ECOLI_DATA)
            
SELECT 
    E.ID,
    CASE
        WHEN A.PCT > 0.75 THEN 'LOW'
        WHEN A.PCT > 0.5 THEN 'MEDIUM'
        WHEN A.PCT > 0.25 THEN 'HIGH'
        ELSE 'CRITICAL'
    END AS COLONY_NAME
FROM 
    ECOLI_DATA E
JOIN
    A
ON 
    E.ID = A.ID
ORDER BY
    E.ID;
    