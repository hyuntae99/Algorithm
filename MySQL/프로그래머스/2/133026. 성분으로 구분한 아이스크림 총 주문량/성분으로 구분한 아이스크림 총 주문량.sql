-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY F.TOTAL_ORDER;