SELECT 
    USER_ID, 
    PRODUCT_ID 
FROM 
    ONLINE_SALE 
GROUP BY 
    USER_ID, 
    PRODUCT_ID
HAVING 
    COUNT(ONLINE_SALE_ID) > 1
ORDER BY 
    USER_ID, 
    PRODUCT_ID DESC;