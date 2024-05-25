SELECT 
    A.APNT_NO, 
    P.PT_NAME, 
    P.PT_NO, 
    D.MCDP_CD, 
    D.DR_NAME, 
    A.APNT_YMD
FROM
    PATIENT P,
    DOCTOR D,
    APPOINTMENT A
WHERE
    A.PT_NO = P.PT_NO
    AND A.MDDR_ID = D.DR_ID
    AND A.APNT_YMD LIKE '2022-04-13%'
    AND A.APNT_CNCL_YN = 'N'
ORDER BY 
    A.APNT_YMD;