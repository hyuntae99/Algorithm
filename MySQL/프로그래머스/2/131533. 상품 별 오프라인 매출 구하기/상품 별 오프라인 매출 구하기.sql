-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(P.PRICE * O.SALES_AMOUNT) AS SALES
FROM PRODUCT P, OFFLINE_SALE O
WHERE P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;