SELECT
    MCDP_CD AS "진료과코드",
    COUNT(MCDP_CD) AS "5월예약건수" 
FROM
    APPOINTMENT  
WHERE
    SUBSTR(APNT_YMD, 6, 2) = "05"
GROUP BY
    MCDP_CD
ORDER BY
    COUNT(MCDP_CD) ASC,
    MCDP_CD ASC
;

-- 틀림 처리받은 것
ORDER BY
    "진료과코드" ASC,
    MCDP_CD ASC
;
