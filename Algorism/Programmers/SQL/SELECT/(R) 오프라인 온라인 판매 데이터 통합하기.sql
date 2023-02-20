SELECT
    substr(SALES_DATE, 1, 10) AS SALES_DATE, 
    PRODUCT_ID, 
    USER_ID, 
    SALES_AMOUNT
FROM
    (
        (
            SELECT 
                SALES_DATE, 
                PRODUCT_ID, 
                USER_ID, 
                SALES_AMOUNT
            FROM 
                ONLINE_SALE
            WHERE
                substr(SALES_DATE, 1, 7) = '2022-03'
        )
        UNION
        (
            SELECT 
                SALES_DATE,	
                PRODUCT_ID, 
                IF(PRODUCT_ID, NULL, NULL) AS USER_ID, 
                SALES_AMOUNT
            FROM 
                OFFLINE_SALE
            WHERE
                substr(SALES_DATE, 1, 7) = '2022-03'
        )
    ) AS C
ORDER BY
    SALES_DATE ASC,
    PRODUCT_ID ASC,
    USER_ID ASC
;