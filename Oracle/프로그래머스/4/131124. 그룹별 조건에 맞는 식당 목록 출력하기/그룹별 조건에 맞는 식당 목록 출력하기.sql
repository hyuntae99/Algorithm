SELECT M.MEMBER_NAME, 
       R.REVIEW_TEXT, 
       TO_CHAR(R.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE M, REST_REVIEW R
WHERE M.MEMBER_ID = R.MEMBER_ID
  AND M.MEMBER_ID = (
                        SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        ORDER BY COUNT(*) DESC
                        FETCH FIRST 1 ROW ONLY
                    )
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT;