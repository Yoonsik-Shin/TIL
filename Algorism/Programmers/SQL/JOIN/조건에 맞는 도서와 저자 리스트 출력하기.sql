SELECT
    A.BOOK_ID,
	B.AUTHOR_NAME,
    substr(A.PUBLISHED_DATE, 1, 10) AS PUBLISHED_DATE
FROM
    BOOK AS A JOIN AUTHOR AS B
    ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE
    A.CATEGORY = '경제'
ORDER BY
    A.PUBLISHED_DATE
;