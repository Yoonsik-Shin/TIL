SELECT
    count(*) AS USERS
FROM
    USER_INFO 
WHERE
    substr(JOINED, 1, 4) = 2021
    AND AGE <= 29
    AND AGE >= 20
;