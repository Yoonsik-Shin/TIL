-- 코드를 입력하세요
SELECT 
    DR_NAME, 
    DR_ID, 
    MCDP_CD, 
    substr(HIRE_YMD, 1, 10)
FROM
    DOCTOR
WHERE
    MCDP_CD = 'CS'
    OR MCDP_CD = 'GS'
ORDER BY
    HIRE_YMD DESC,
    DR_NAME ASC