# 2세대 구하는 서브쿼리
WITH J 
    AS (SELECT A.ID
        FROM ECOLI_DATA A
        JOIN ECOLI_DATA B
        ON A.PARENT_ID = B.ID
        WHERE B.PARENT_ID IS NULL) # 부모가 없는 경우 -> 1세대)

SELECT 
    A.ID
FROM 
    ECOLI_DATA A
JOIN 
    J ON A.PARENT_ID = J.ID # 2세대를 부모로 하는 = 3세대
ORDER BY 
    ID;