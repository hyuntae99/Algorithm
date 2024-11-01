# 백분위로 순서를 부여
WITH A
    AS (SELECT 
            *, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PCT
        FROM 
            ECOLI_DATA)
            
SELECT 
    E.ID,
    CASE 
        WHEN A.PCT <= 0.25 THEN 'CRITICAL'
        WHEN A.PCT <= 0.5 THEN 'HIGH'
        WHEN A.PCT <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM 
    ECOLI_DATA E
JOIN
    A
ON 
    E.ID = A.ID
ORDER BY
    E.ID;