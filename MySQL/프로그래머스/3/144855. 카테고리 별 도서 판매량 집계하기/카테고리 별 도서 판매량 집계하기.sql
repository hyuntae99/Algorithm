-- 코드를 입력하세요
SELECT 
    B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM 
    BOOK B, BOOK_SALES S
WHERE
    B.BOOK_ID = S.BOOK_ID
    AND S.SALES_DATE LIKE '2022-01%'
GROUP BY 
    B.CATEGORY
ORDER BY 
    CATEGORY;