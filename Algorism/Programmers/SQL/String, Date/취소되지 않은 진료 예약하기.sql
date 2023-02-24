SELECT
    C.APNT_NO,
    D.PT_NAME,
    C.PT_NO,
    C.MCDP_CD,
    C.DR_NAME,
    C.APNT_YMD
FROM
    (
        SELECT
            B.MCDP_CD,
            B.DR_NAME,
            A.PT_NO,
            A.APNT_CNCL_YN,
            A.APNT_CNCL_YMD,
            A.APNT_NO,
            A.APNT_YMD
        FROM
            APPOINTMENT AS A JOIN DOCTOR AS B
            ON A.MDDR_ID = B.DR_ID
    ) AS C 
    JOIN PATIENT AS D
    ON C.PT_NO = D.PT_NO
WHERE
    C.APNT_CNCL_YN = 'N' AND DATE_FORMAT(C.APNT_YMD, "%Y-%m-%d") = "2022-04-13"
ORDER BY
    C.APNT_YMD
;