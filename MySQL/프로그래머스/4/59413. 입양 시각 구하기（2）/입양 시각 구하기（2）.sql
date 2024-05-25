-- 시간대 테이블 생성
WITH RECURSIVE hours AS (
    SELECT 0 AS hour
    UNION ALL
    SELECT hour + 1
    FROM hours
    WHERE hour < 23
)

-- 동물 출타 기록 집계
SELECT 
    h.hour AS HOUR, 
    COUNT(DISTINCT a.ANIMAL_ID) AS COUNT
FROM 
    hours h
LEFT JOIN 
    ANIMAL_OUTS a ON h.hour = HOUR(a.DATETIME)
GROUP BY 
    h.hour
ORDER BY 
    h.hour;