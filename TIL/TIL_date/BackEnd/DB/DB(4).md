# DB (4)

## 기타 구문 정리    

### 1️⃣ CASE문

- 특정 상황에서 데이터를 변환하여 활용
- ELSE 생략 시 NULL값 지정

```sql
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
```

```sql
# 예시
SELECT
	last_name,
	age,
	CASE
		WHEN age < 18 THEN '청소년'
		WHEN age <= 30 THEN '청년'
		WHEN age <= 64 THEN '중장년'
		ELSE '기타'
	END
FROM users
LIMIT 15;
```

​    

---

### 2️⃣ 서브쿼리

- 특정한 값을 메인 쿼리에 반환하여 활용

- 실제 테이블에 없는 기준을 이용한 검색 가능

- __소괄호__로 감싸서 활용

- 메인 쿼리의 컬럼 모두 사용가능 / ❗메인 쿼리는 서브 쿼리의 컬럼 사용 불가

```sql
SELECT *
FROM <테이블명>
WHERE <컬럼1> = (
		SELECT <컬럼1>
		FROM <테이블명>
);
```

​    

#### 단일행 서브쿼리

- 서브쿼리의 결과가 0 or 1 개인 경우
- 주로 단일행 비교 연산자와 함께 사용 (`=, <, >, <>`)

1. WHERE절에서의 활용

```sql
-- 예시 : 가장 나이가 적은 사람의 수
SELECT count(*)
FROM <테이블명>
WHERE age = (SELECT MIN(age) FROM <테이블명>);
```

​    

2. SELECT절에서의 활용

```sql
-- 예시 : 전체 인원과 평균 연봉, 평균 나이
SELECT
		(SELECT count(*) FROM users) AS 총인원,
		(SELECT AVG(balance) FROM users) AS 평균연봉,
		(SELECT AVG(age) FROM users) AS 평균나이
;
```

​    

3. UPDATE에서 활용

```sql
-- 예시 : users 테이블의 모든 잔고값을 평균 잔고값으로 바꾸기 
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```

​    

#### 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우
- 주로 다중행 비교 연산자와 함께 사용 (`IN, EXISTS`)

```sql
-- 예시 : a라는 이름을 갖는 사람과 같은 지역에 사는 사람의 수
SELECT count(*)
FROM users
WHERE country IN(
		SELECT country
		FROM users
		WHERE name = 'a'
);
```

​    

#### 다중컬럼 서브쿼리

```sql
-- 예시 : 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT
	last_name,
	first_name,
	age
FROM users
WHERE (last_name, age) IN(
	SELECT last_name, Min(age)
	FROM users
	GROUP BY last_name)
ORDER BY last_name;
```

​    

---

### 3️⃣ View

- 논리(가상)의 테이블
- 자주 사용하는 쿼리문 결과를 하나의 테이블처럼 만들어 조회할 수 있게 해줌 
- view에서 데이터를 직접 삭제할 수 없음
- CUD를 할 수 있는 view도 존재
- view 생성

```sql
CREATE VIEW 뷰이름 AS 
쿼리문;
```

- 이미 존재하는 view를 새 쿼리로 대체/교체하기

```sql
-- 방법1
CREATE VIEW REPLACE VIEW 뷰이름 AS 
쿼리문;

-- 방법2
ALTER VIEW 뷰이름 AS
쿼리문;
```

- view 삭제

```sql
DROP VIEW 뷰이름;
```

​    

----

### 4️⃣ 날짜 / 시간 다루기

- 현재 날짜 + 시간 : `NOW`, `CURRENT_TIMESTAMP`

```sql
-- yyyy-mm-dd hh:mm:ss
SELECT NOW()
select CURRENT_TIMESTAMP();
>> 2023-02-23 00:00:00
```

- 현재 날짜 : `CURDATE`, `CURRENT_DATE`

```sql
-- yyyy-mm-dd / 2023-07-10
select curdate();
select CURRENT_DATE();
```

- 현재 시간 : `CURTIME`, `CURRENT_TIME`

```sql
-- hh:mm:ss / 15:30:20
select curtime();
select CURRENT_TIME();
```

- 날짜 / 시간 형식 변환 : `DATE_FORMAT`

```sql
 SELECT DATE_FORMAT(NOW(), "%Y-%m")
 >> 2023-02
 
 SELECT DATE_FORMAT(NOW(), "%Y")
 >> 2023
```

> format 종류

| 구분자 | 설명               |
| ------ | ------------------ |
| %d     | 00 ~ 31일          |
| %e     | 0 ~ 31일           |
| %H     | 00 ~ 23시          |
| %k     | 0 ~ 23시           |
| %h     | 01 ~ 12시          |
| %l     | 1 ~ 12시           |
| %M     | January ~ December |
| %m     | 00 ~ 12월          |
| %U     | 00 ~ 53주 (일)     |
| %u     | 00 ~ 53주 (월)     |
| %Y     | 4자리 연도         |
| %y     | 2자리 연도         |

- 날짜 더하기 빼기 : `DATE_ADD`, `DATE_SUB`

```sql
SELECT DATE_ADD('2022-02-23', INTERVAL 1 DAY); -- 날짜에 하루를 더합니다.
>> 2022-02-24

SELECT DATE_SUB('2022-02-23', INTERVAL 1 WEEK); -- 날짜에서 일주일을 뺍니다.
>> 2022-02-16
```

- 날짜 차이 계산하기 : `DATEDIFF`

> ❗주의점 : 1일 차이 주의

```sql
SELECT DATEDIFF('2022-02-28', '2022-02-23'); -- 두 날짜 간의 차이(일)를 계산합니다.
>> 5
```

- 날짜 비교 (`비교연산자`)

```sql
-- order_date가 2022-02-23 이후인 주문 정보를 조회합니다.
SELECT * FROM orders WHERE order_date > '2022-02-23'; 
```

- 날짜 추출하기 (`YEAR`, `MONTH`, `DAY`)

```sql
SELECT YEAR('2022-02-23'); -- 날짜에서 연도를 추출합니다.
SELECT MONTH('2022-02-23'); -- 날짜에서 월을 추출합니다.
SELECT DAY('2022-02-23'); -- 날짜에서 일을 추출합니다.
```

- 날짜 요일 추출하기 (`DAYOFWEEK`, `DATYNAME`)

```sql
-- 요일에 대한 숫자반환
SELECT DAYOFWEEK(date); 
>> 일: 1, 월: 2, ..., 토: 7

-- 요일이름 반환
SELECT DAYNAME(date);
>> Monday, Tuesday
```



- 연월 단위로 그룹핑

```sql
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS order_month, 
    COUNT(*) AS orders_count
FROM 
    orders
GROUP BY
    order_month;
```

​    

- 시간 추출하기

```sql
SELECT YEAR('2022-02-23'); -- 날짜에서 연도를 추출합니다.
SELECT MONTH('2022-02-23'); -- 날짜에서 월을 추출합니다.
SELECT DAY('2022-02-23'); -- 날짜에서 일을 추출합니다.
```

​    

---

### 5️⃣ 원도우 함수

- window라는 특정한 방식으로 파이션을 분할하여 값을 연산
- 집계함수와 함께 사용
- 모든 행마다 값이 출력

​    

#### OVER

1. PARTITION BY

```sql
SELECT 
	emp_no, 
	department, 
	salary, 
	AVG(salary) OVER(PARTITION BY department) AS dept_avg
FROM emps;
```

| emp_no | department       | salary |
| ------ | ---------------- | ------ |
| 1      | sales            | 59000  |
| 2      | sales            | 60000  |
| 10     | customer service | 56000  |
| 11     | customer service | 55000  |

- sales window

| emp_no | department | salary |
| ------ | ---------- | ------ |
| 1      | sales      | 59000  |
| 2      | sales      | 60000  |

- customer service window

| emp_no | department       | salary |
| ------ | ---------------- | ------ |
| 10     | customer service | 56000  |
| 11     | customer service | 55000  |

- 결과

| emp_no | department       | salary | dept_avg   |
| ------ | ---------------- | ------ | ---------- |
| 1      | sales            | 59000  | 55500.0000 |
| 2      | sales            | 60000  | 55500.0000 |
| 10     | customer service | 56000  | 59500.0000 |
| 11     | customer service | 55000  | 59500.0000 |



2. ORDER BY

- 각 window에 속한 행의 순서 변경

```sql
 SELECT 
    emp_no, 
    department, 
    salary, 
    SUM(salary) OVER(PARTITION BY department ORDER BY salary) AS rolling_dept_salary,
    SUM(salary) OVER(PARTITION BY department) AS total_dept_salary
FROM employees;
```

