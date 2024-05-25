-- 코드를 입력하세요
SELECT 
    YEAR(S.SALES_DATE) AS YEAR, 
    MONTH(S.SALES_DATE) AS MONTH, 
    U.GENDER, 
    COUNT(DISTINCT U.USER_ID) AS USERS
FROM
    USER_INFO U, ONLINE_SALE S
WHERE 
    U.USER_ID = S.USER_ID
    AND U.GENDER IS NOT NULL
GROUP BY 
    YEAR, MONTH, U.GENDER
ORDER BY 
    YEAR, MONTH, U.GENDER