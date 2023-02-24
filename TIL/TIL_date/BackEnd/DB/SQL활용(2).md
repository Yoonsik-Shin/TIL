# SQL문 활용 (2)

​    

## ✍️ SELECT - SQL 기본함수, 연산

### 1. 문자열 함수

```sql
SUBSTR(문자열, start, length) # 문자열 자르기 (시작 인덱스 = 1, 마지막 인덱스 = -1)
TRIM(문자열)                  # 문자열 공백제거
LTRIM(문자열)                 # 문자열 왼쪽 공백제거
RTRIM(문자열)                 # 문자열 오른쪽 공백제거
LENGTH(문자열)                # 문자열 길이
REPLACE(문자열, 패턴, 변경값)  # 문자열 변경
UPPER(문자열)                 # 대문자 변경
LOWER(문자열)                 # 소문자 변경 
||                            # 문자열 합치기 (concatenation)
```

​    

### 2. 숫자 함수

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

### 3. 산술연산자

-  `+`, `-`, `*`, `/` 와 () 활용가능

```sql
SELECT age+1 FROM users;
```

​    

> ALIAS

- 컬럼명이나 테이블명이 길어 다른 명칭으로 확인하고 싶을때 사용
- AS를 생략하여 공백으로 표현가능
- 별칭에 공백이나 특수문자 있을 경우 `" "`로 묶어 표기

```sql
SELECT last_name 성 FROM users;
SELECT last_name AS 성 FROM users;
SELECT last_name AS "이름 성" FROM users WHERE "이름 성" = '김';
```

​    

### 4. GROUP BY

- 문장에 WHERE절이 포함된 경우 반드시 WHERE절 뒤에 작성
- 지정된 컬럼의 값이 같은 행들로 묶음
- ✔️ 집계함수와 활용하였을 때 의미가 있음 ❗
- GROUP BY의 결과는 정렬되지 않음 > ORDER BY를 통해 정렬

```sql
SELECT * FROM <테이블명> GROUP BY 컬럼1, 컬럼2, ...;
```

​    

### 5. HAVING

- 집계함수는 WHERE절의 조건식 사용 불가 (실행 순서가 다름)
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해 사용

```sql
SELECT * FROM <테이블명> GROUP BY 컬럼1, 컬럼2, ... HAVING 그룹조건;
```



### ♾️ SELECT 문장 실행 순서

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

## ✍️ ALTER (DDL)

1. 테이블 이름 변경

```sql
ALTER TABLE <변경전 테이블명>
RENAME TO <변경후 테이블명>;
```

​    

2. 새로운 컬럼 추가

```sql
ALTER TABLE <테이블명>
ADD COLUMN <새로 추가할 컬럼명>
```

​    

3. 컬럼명 이름 수정

```sql
ALTER TABLE <테이블명>
RENAME COLUMN <변경전 컬럼명> TO <변경후 컬럼명>
```

​    

4. 컬럼 삭제

```sql
ALTER TABLE <테이블명>
DROP COLUMN <삭제할 컬럼명>
```

​    

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

