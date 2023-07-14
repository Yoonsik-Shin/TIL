# DB (3)

## DML

### 1️⃣ SELECT

- 테이블 데이터 조회

​    

#### 1. 실행 순서

- FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY

```sql
SELECT 컬럼명 # 5. 조회하여
FROM 테이블명 # 1. 테이블을 대상으로
WHERE 조건식  # 2. 제약조건을 맞춰 뽑아
GROUP BY 컬럼 / 표현식 # 3. 그룹화한다.
HAVING 그룹조건식 # 4. 그 그룹 중에서 조건과 맞는것들만 >> SELECT 5. 조회하여
ORDER BY 컬럼 / 표현식 # 6. 정렬하고
LIMIT 숫자 OFFSET 숫자; # 7. 특정 위치의 값을 가져온다.
```

​    

#### 2. 별칭 (Alias)

- 컬럼명이나 테이블명이 길어 다른 명칭으로 확인하고 싶을때 사용
- AS를 생략하여 공백으로 표현가능
- 별칭에 공백이나 특수문자 있을 경우 `" "`로 묶어 표기

```sql
SELECT last_name 성 FROM users;
SELECT last_name AS 성 FROM users;
SELECT last_name AS "이름 성" FROM users WHERE "이름 성" = '김';
```

​    

#### 3. 절 (Clause)

##### WHERE

- 특정 조건으로 데이터 조회

```sql
SELECT * FROM <테이블명> WHERE 조건;
```

​     

> WHERE절에서 사용할 수 있는 연산자

1. 비교연산자

   - 기본적으로 대소문자를 구분하지 않음

   ```sql
   WHERE name = "shin"
   WHERE age <= 34
   WHERE year >= 2000
   ```

2. 논리연산자

   - 종류 : `AND`, `OR`, `NOT`
   - 조건이 true면 1 반환, false이면 0 반환
   - 논리 연산자 주의사항

   ```sql
   -- 1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
   WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
   -- 2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
   WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80

3. BETWEEN `a` AND `b`

   - a이상 b이하

   ```sql
   WHERE 컬럼 BETWEEN a AND b
   WHERE 컬럼 NOT BETWEEN a AND b
   ```

4. IN(`a`, `b`, `c`, ...)
   - IN 속 목록중 값이 하나라도 일치할 때

   ```sql
   WHERE 컬럼 IN ('a', 'b', 'c')
   WHERE 컬럼 NOT IN ('a', 'b', 'c')
   ```

5. LIKE

   - 비교 문자열과 형태 일치

   - 패턴이 일치하는 데이터를 조회하는 방법

   - SQLite 와일드카드 2가지

     - `%` (percent sign) : 0개 이상의 문자, ❗자리에 문자열이 있을수도, 없을 수도 있음❗
     - `_` (underscore) : 임의의 단일 문자,  ❗반드시 이 자리에 한 개의 문자가 존재해야함❗

     ```sql
     SELECT * FROM <테이블명> WHERE <컬럼> LIKE '패턴';
     SELECT * FROM <테이블명> WHERE <컬럼> NOT LIKE '패턴';
     ```
     
     > 패턴 예시
     
     | 패턴           | 의미                                          |
     | -------------- | --------------------------------------------- |
     | 2%             | 2로 시작하는 값                               |
     | %2             | 2로 끝나는 값                                 |
     | %2%            | 2가 들어가는 값                               |
     | _2%            | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
     | 1___           | 1로 시작하고 총 4자리인 값                    |
     | 2\_%\_% / 2__% | 2로 시작하고 적어도 3자리인 값                |

6. IS NULL / IS NOT NULL

   - null인 행 다루기

   ```sql
   -- NULL인 행만 가져오기
   WHERE 컬럼명 IS NULL
   
   -- NULL이 아닌 행만 가져오기
   WHERE 컬럼명 IS NOT NULL 
   
   -- 틀린방법
   WHERE 컬럼명 = NULL 
   ```

7. 부정연산자

   - 같지 않다 (`!=`, `^=`, `<>`)
   - ~와 같지 않다 (`NOT 컬럼 = 비교값`)

   ```sql
   WHERE 칼럼명1 != 비교값1 
   AND 칼럼명2 ^= 비교값2 
   AND 칼럼명3 <> 비교값3 
   AND NOT 칼럼명4 = 비교값4 
   AND NOT 칼럼명5 > 비교값5; 
   ```

​    

>  연산자 우선순위

| 순위 | 연산자          |
| ---- | --------------- |
| 1    | 괄호 ()         |
| 2    | NOT             |
| 3    | 비교연산자, SQL |
| 4    | AND❗            |
| 5    | OR❗             |

​    

##### GROUP BY

- 문장에 WHERE절이 포함된 경우 반드시 WHERE절 뒤에 작성
- 지정된 컬럼의 값이 같은 행들로 묶음
- ✔️ 집계함수와 활용하였을 때 의미가 있음 ❗
- GROUP BY의 결과는 정렬되지 않음 > ORDER BY를 통해 정렬

```sql
SELECT 컬럼명 FROM <테이블명> GROUP BY 컬럼명;
SELECT 컬럼명, 집계함수 FROM <테이블명> GROUP BY 컬럼명;
SELECT 컬럼명1 FROM <테이블명> GROUP BY 컬럼명1, 컬럼명2, ...;
```

​    

##### HAVING

- 집계함수는 WHERE절의 조건식 사용 불가 (실행 순서가 다름)
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해 사용

```sql
SELECT * FROM <테이블명> GROUP BY 컬럼1, 컬럼2, ... HAVING 그룹조건;
```

​    

##### ORDER BY

- 조회 결과 집합을 정렬

```sql
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;    # ASC  : 오름차순 (default)
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;   # DESC : 내림차순
```

- 또다른 사용법 (자주 사용안됨)

``` sql
SELECT a열, b열, c열 FROM 테이블이름 ORDER BY 2;   # b열 기준 정렬
```

- 다중 열 정렬

```sql
SELECT a열, b열, c열, d열 FROM 테이블이름 ORDER BY b열, c열
```

> b열이 정렬된 이후, b열을 기준으로 c열을 정렬

| b열 (정렬됨) | c열  |
| ------------ | ---- |
| a            | 100  |
| a            | 20   |
| b            | 1000 |
| b            | 200  |
| c            | 3000 |
| c            | 4000 |
| c            | 100  |

| b열 (정렬됨) | c열 (정렬됨) |
| ------------ | ------------ |
| a            | 20           |
| a            | 100          |
| b            | 200          |
| b            | 1000         |
| c            | 100          |
| c            | 3000         |
| c            | 4000         |

​    

##### LIMIT 

- 쿼리에서 반환되는 __행 수__ 제한
- 특정 행부터 시작하여 조회하기 위해 OFFSET과 함께 사용 가능

```sql
SELECT 컬럼1, 컬럼2, ... FROM <테이블명> LIMIT <조회할 컬럼수> OFFSET <'숫자' 이후부터 시작>;

-- 예시
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid name
----- ----
3            이동영
```

​    

##### OFFSET

- 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

```sql
SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5;
-- 해석
6번째 행부터 10개의 행 조회 (6행부터 10개 출력)
-- 주의사항
OFFSET은 인덱스처럼 0부터 시작
```

​    

##### DISTINCT

- 조회 결과에서 중복행 제거
- DISTINCT절은 SELECT 키워드 바로 뒤에 작성

```sql
SELECT DISTINCT 컬럼 FROM <테이블명>;
```

​    

#### 4. 문자열 함수

```sql
SUBSTR(문자열, start, length)    # 문자열 자르기 (시작 인덱스 = 1, 마지막 인덱스 = -1)
SUBSTRING(문자열, start, length) # 문자열 자르기 (SUBSTR과 동일)
LEFT(문자열, length)             # 문자열 왼쪽에서부터 length만큼 글자수 불러오기
RIGHT(문자열, length)            # 문자열 오른쪽에서부터 length만큼 글자수 불러오기
REPEAT(문자열, length)           # 문자열을 length만큼 반복하여 불러옴
LENGTH(문자열)                   # 문자열 길이
REPLACE(문자열, 패턴, 변경값)     # 문자열 변경 (대소문자 구분O)
REVERSE(문자열)                  # 문자열 뒤집기
UPPER/UCASE(문자열)              # 대문자 변경
LOWER/LCASE(문자열)              # 소문자 변경 
LENGTH(문자열)                   # 바이트수 반환
CHAR_LENGTH(문자열)              # 문자열 개수 반환
CONCAT(x, y, z)                 # 문자열 합치기 (concatenation)
CONCAT_WS("구분자", x, y, z)     # 구분자로 문자열 합치기 (concatenation)
||                              # 문자열 합치기 (concatenation)
TRIM(문자열)                     # 문자열 가장 왼쪽과 오른쪽 공백제거 (중간 공백은 제거x)
TRIM(LEADING 'x' FROM 문자열)    # 문자열 왼쪽의 x만 제거
TRIM(BOTH '' FROM 문자열)        # 문자열 왼쪽, 오른쪽 x 제거
TRIM(TRAILING 'x' FROM 문자열)   # 문자열 오른쪽의 x만 제거
LTRIM(문자열)                    # 문자열 왼쪽 공백제거
RTRIM(문자열)                    # 문자열 오른쪽 공백제거
```

​    

#### 5. 숫자 함수

```sql
ABS(숫자)         # 절대값
SIGN(숫자)        # 부호
MOD(A, B)         # A를 B로 나눈 나머지
CEIL(숫자)        # 올림
FLOOR(숫자)       # 내림
ROUND(숫자, 반올림할 자리수)  # 반올림
POWER(a, b)       # 제곱 (a의 b제곱)
SQRT(숫자)        # 제곱근
```

​    

#### 6. 산술연산자

-  `+`, `-`, `*`, `/` 와 () 활용가능

```sql
SELECT age+1 FROM users;
```

​    

#### 7. 집계함수

- Aggregate Function
- 값의 집합에 대한 계산을 수행하고 `단일값` 반환 ( = 여러행으로부터 하나의 결과값 반환)
- Group By도 포함
- SELECT 구문에서만 사용가능 ❗

> 집계함수 종류

1. COUNT : 그룹의 항목수

```sql
SELECT COUNT(컬럼명) FROM 테이블명
SELECT COUNT(DISTINCT 컬럼명) FROM 테이블명;
```

2. AVG : 평균

````sql
SELECT AVG(컬럼명) FROM 테이블명;
````

3. MAX / MIN
   - 숫자일 경우, 최대/최소값 반환
   - 문자일 경우, 알파벳 순서중 가장 앞/뒤에 있는 값 반환

```sql
SELECT MAX(컬럼명) FROM 테이블명;
SELECT MIN(컬럼명) FROM 테이블명;
```

4. SUM
   - 문자일 경우, 0으로 취급

```sql
SELECT SUM(컬럼명) FROM 테이블명;
```

​    

#### 8. 기타

1. Alias 설정시 주의사항 : 한글 띄어쓰기 사용시 작은 따옴표 대신 `큰 따옴표 ("")` 사용해야함
2. strftime

```sql
-- strftime 함수 > 문자열로 반환
strftime('형식', 컬럼) 

-- 예시
strftime('%Y', 컬럼명)
>> '2013'
```

3. CAST

```sql
-- cast 함수 : 형식변환
cast(바꿀값 as int) 
```

4. IFNULL

```sql
-- 표현식이 NULL인 값을 조작하는 함수
SELECT IFNULL(평가식, null일경우나타낼것) FROM ...
```



---

### 2️⃣ INSERT

```sql
-- 단일 행 삽입
INSERT INTO <테이블명> (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);

-- 모든 컬럼에 맞춰 순서대로 입력
INSERT INTO <테이블명> VALUES (값1, 값2, 값3, ...);
```

​    

---

### 3️⃣ UPDATE

```sql
UPDATE <테이블명> SET <컬럼명>="바꿀컬럼값" WHERE <조건>;
```

​    

---

### 4️⃣ DELETE

```sql
-- 테이블의 모든행 삭제
DELETE FROM <테이블명>

-- 특정행만 삭제
DELETE FROM <테이블명> WHERE <조건>;
```

> UPDATE / DELETE 명령어전에 where절을 select하여 실수를 방지함

​    

---

## ✍️ 예제

1. 테이블 만들기
   - 컬럼명 : tilte, content
   - 테이블명 : articles
   - 조건 : 두 컬럼 모두 비어있으면 안됨, rowid 사용

```sql
CREATE TABLE articles(
  title TEXT NOT NULL,
  content TEXT NOT NULL
);
```

​    

2. 테이블에 값 추가하기
   - title = '1번제목'
   - content = '1번내용'

```sql
INSERT INTO articles VALUES ('1번제목', '1번내용');
```

​    

3. 테이블 이름 변경하기
   - 새로운 테이블명 : news

```sql
ALTER TABLE articles RENAME TO news;
```

​    

4. 새로운 컬럼 추가하기
   - 새 컬럼명 : created_at
   - 타입 : TEXT
   - 기타조건 : NULL값 없어야함

```sql
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
-- 오류 발생
-- Error : Cannot add a NOT NULL column with default value NULL
❗테이블에 있던 기존 레코드들에 새로 추가될 필드에 대한 정보가 없다.
```

​    

> 오류해결 방법

1. NOT NULL 설정없이 추가하기

```sql
ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO articles VALUES ('제목', '내용', '값');
```

​    

2. 기본값 (DEFAULT) 설정하기

```sql
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
```

