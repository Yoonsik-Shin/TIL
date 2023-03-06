
SELECT ABS(-100); -- 절대값
SELECT MOD(14, 3), 14 % 3, 14 MOD 3; -- 나머지
SELECT POW(3, 2), SQRT(16); -- 제곱, 제곱근

SELECT CEILING(3.7), FLOOR(3.7), ROUND(3.7); -- 올림, 버림, 반올림
SELECT CEILING(3.789, 2), FLOOR(3.789, 2), ROUND(3.789, 2);

SELECT RAND(); -- 랜덤
SELECT TRUNCATE(1234.6789, 2), TRUNCATE(1234.6789, -2); -- 버림


SELECT ASCII('A');  -- 아스키 코드 반환
SELECT CHAR(65); -- 아스키 코드에 맞는 문자 반환



SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc'); -- 문자열 비트길이 , 문자길이(단위), 총 문자 길이 
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');



SELECT CONCAT('2020', '01', '01'); -- 붙이는 함수
SELECT CONCAT_WS('-','2020', '01', '01'); -- 구분자 추가하여 붙이는 함수



SELECT INSTR('abcd', 'b'); -- 첫번째 파라미터에서 두번째 파라미터를 검색하여 나온 갯수 반환 



SELECT FORMAT(123456789.1234, 2); -- 소수점 표현
SELECT LPAD('1234', 6, '0'), RPAD('1234', 6, '0');  -- 첫번째 파라미터에서 받은 데이터를 세번째 파라미터로 받은 문자열을 이용해 두번째 파라미터에 넣은 숫자 만큼 늘림,
SELECT LTRIM('   abc'), RTRIM('abc   '), TRIM('  abc  '); -- 공백 제거 (trim)


SELECT TRIM(BOTH 'a' FROM 'aababaa'); -- 문자 제거(trim)


SELECT LEFT('가나다라마바', 3), RIGHT('가나다라마바', 3); -- 첫째 파라미터에 받은 문자열에서 두번쨰 파라미터로 받은 숫자만큼 자름 
SELECT LCASE('aBcDe'), UCASE('aBcDe'); -- 대문자, 소문자
SELECT LOWER('aBcDe'), UPPER('aBcDe');
SELECT MID('aBcDe', 2, 3); -- 문자열, 시작위치, 갯수


SELECT REPLACE ('It is banana', 'banana', 'apple'); -- 대체
SELECT SUBSTRING('abcdef', 3, 2);   -- 문자열, 시작위치, 길이


SELECT SUBSTRING_INDEX('aaa,bbb,ccc,ddd', ',', 2); -- 두번쨰 파라미터
SELECT SUBSTRING_INDEX('aaa,bbb,ccc,ddd', ',', -2);


SELECT ADDDATE('2020-01-01', INTERVAL 31 DAY), SUBDATE('2020-01-01', INTERVAL 31 DAY);
SELECT DATE_ADD('2020-01-01', INTERVAL -31 DAY), DATE_SUB('2020-01-01', INTERVAL 31 DAY);

SELECT ADDDATE('2020-01-01', INTERVAL -1 HOUR);
SELECT ADDDATE('2020-01-01', INTERVAL -1 MINUTE);
SELECT ADDDATE('2020-01-01', INTERVAL -1 SECOND);



SELECT CURDATE(), CURTIME(), NOW(), SYSDATE();


SELECT YEAR(NOW()), MONTH(NOW()), DAYOFMONTH(NOW()),
       HOUR(NOW()), MINUTE(NOW()), SECOND(NOW()), MICROSECOND(NOW));


SELECT MONTHNAME('20000721'); -- 영어 월이름
SELECT DAYNAME('2001-06-22'); -- 영어 요일이름
SELECT DAYOFWEEK('2003-03-21'); -- 요일 숫자, 월요일(0),화요일(1), ..., 일요일(6)
SELECT WEEKDAY('2003-03-21'); -- same as DAYOFWEEK


SELECT DATE(NOW()), TIME(NOW());
SELECT DATEDIFF('2020-1-5', '2020-1-1'), TIMEDIFF('14:30:00', '06:30:00');
SELECT DAYOFWEEK(NOW()), MONTHNAME(NOW()), DAYOFYEAR(NOW());
SELECT LAST_DAY('2020-02-04'); -- 해당월의 마지막 날짜
SELECT TIME_TO_SEC('10:53:10');


SELECT DATE_FORMAT(NOW(),'%Y-%m-%d') FROM DUAL;
SELECT DATE_FORMAT(NOW(),'%H:%i:%S') FROM DUAL;

SELECT @@GLOBAL.TIME_ZONE, @@SESSION.TIME_ZONE;
SELECT CONCAT_WS(' ', DATE_FORMAT(NOW(),'%H:%i:%S'), @@SESSION.TIME_ZONE) FROM DUAL;

SELECT DATE_FORMAT(CONVERT_TZ(NOW(), 'UTC', 'Asia/Seoul'),'%H:%i:%S') FROM DUAL;

SELECT IF(a>1, 'A', 'B'); -- 조건식, 참일때 반환값, 거짓일때 반환값
SELECT IFNULL(a, 'ERR'); -- 첫번째가 NULL 이면 두번째 값 반환
SELECT COUNT(column), AVG(column), SUM(column), MIN(column), MAX(column);