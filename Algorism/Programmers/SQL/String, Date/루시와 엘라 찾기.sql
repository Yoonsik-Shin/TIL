-- 방법1
SELECT
    ANIMAL_ID, 
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS 
WHERE
    NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY
    ANIMAL_ID
;

-- 방법2
SELECT 
    ANIMAL_ID, 
    NAME, 
    SEX_UPON_INTAKE 
FROM 
    ANIMAL_INS 
WHERE 
    NAME = 'Lucy' 
    OR NAME = 'Ella' 
    OR NAME = 'Pickle' 
    OR NAME = 'Rogan' 
    OR NAME = 'Sabrina' 
    OR NAME = 'Mitty'