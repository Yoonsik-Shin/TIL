SELECT 
    A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, round(avg(B.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_INFO AS A JOIN REST_REVIEW AS B
    ON A.REST_ID = B.REST_ID
WHERE
    substr(ADDRESS, 1, 2) = '서울'
GROUP BY
    A.REST_ID,
    A.REST_NAME
ORDER BY
    SCORE DESC,
    A.FAVORITES DESC
;