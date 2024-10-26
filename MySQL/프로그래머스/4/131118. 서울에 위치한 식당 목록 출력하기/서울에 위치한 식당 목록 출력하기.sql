WITH A 
    AS (SELECT 
            REST_ID, 
            COUNT(*) AS CNT, 
            ROUND(AVG(REVIEW_SCORE),2) AS AVG_SCORE
        FROM 
            REST_REVIEW 
        GROUP BY 
            REST_ID)
        
SELECT 
    I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, A.AVG_SCORE AS SCORE
FROM 
    REST_INFO I
JOIN 
    A ON I.REST_ID = A.REST_ID
WHERE 
    I.ADDRESS LIKE '서울%'
ORDER BY 
    A.AVG_SCORE DESC, A.CNT DESC;

