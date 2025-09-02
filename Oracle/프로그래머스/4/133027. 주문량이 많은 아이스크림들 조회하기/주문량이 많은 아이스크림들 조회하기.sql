select *
  from
(
SELECT J.FLAVOR 
  FROM JULY J
 GROUP BY J.FLAVOR
 ORDER BY SUM(J.TOTAL_ORDER) + (SELECT SUM(F.TOTAL_ORDER)
                                  FROM FIRST_HALF F
                                 WHERE J.FLAVOR = F.FLAVOR) DESC
)
where rownum <= 3