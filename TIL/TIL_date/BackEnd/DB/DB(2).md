# DB (2)    

## 1️⃣ DB Manage

- 모든 데이터베이스 보기

```sql
mysql> show databases;
```

![image-20230704133429871](DB(2).assets/image-20230704133429871.png)

- 데이터베이스 생성

```sql
mysql> create database <데이터베이스명>;
```

- 데이터베이스 삭제

```sql
mysql> drop database <데이터베이스명>;
```

- 데이터베이스 사용 / 확인

```sql
mysql> use <데이터베이스명>;

# 사용중인 DB 보기
mysql> select database();
```

> DB 이름변경

- 잘못 이름을 변경하면 문제가 생길 수 있기 때문에 명령어가 따로 존재하지 않음
- `mysqldump`를 통해 새로운 DB에 기존 데이터를 옮기는 식으로 구현해야함

1. 기존 DB dump

```bash
$ mysqldump -u root -p 기존DB명 > 기존DB명.sql

# 프로시저도 같이 옮긴다면
$ mysqldump -u root -p --routines 기존DB명 > 기존DB명.sql
```

2. 새 DB 생성

```bash
$ mysql -u root -p -e "CREATE DATABASE 새DB명"
```

3. 기존 DB dump파일을 새 DB에 옮김

```bash
$ mysql -u root -p 새DB명 < 기존DB명.sql
```

4. 기존 DB 삭제 (옵션)

```bash
$ mysql -u root -p -e "DROP DATABASE 기존DB명"
```

​    

---

## 2️⃣ Data Type

### 1. Text

- 텍스트 저장

#### Char

- 크기가 고정되어있어 문자열이 같은 크기를 가짐
- 저장한 문자열이 지정한 크기보다 작으면 오른쪽에 공백을 추가하여 지정한 크기에 맞춰 저장
- 검색할 때는 공백이 제거되어 검색됨
- 0 ~ 255사이의 값을 가짐
- 나라코드, 우편번호, 전화번호

```sql
create table 테이블명(
	컬럼명1 char(2),  -- 무조건 두개의 문자열로 저장됨
)
```

​    

#### Varchar

- 최대길이를 지정할 수 있음

```sql
create table 테이블명(
    컬럼명2 varchar(31)
)
```

- Char가 모든 문자열의 크기가 비슷한 경우에는 저장공간 활용면에서는 더 효율적

​    

### 2. Number

#### INT

- 정수 저장
- `unsigned` : 음수를 제외한 양수부분만 사용

| Type        | Bytes | 최소값 (Signed) | 최소값 (Unsigned) | 최대값 (Signed) | 최대값 (Unsigned) |
| ----------- | ----- | --------------- | ----------------- | --------------- | ----------------- |
| `TINYINT`   | 1     | `-128`          | `0`               | `127`           | `255`             |
| `SMALLINT`  | 2     | `-32768`        | `0`               | `32767`         | `65535`           |
| `MEDIUMINT` | 3     | `-8388608`      | `0`               | `8388607`       | `16777215`        |
| `INT`       | 4     | `-2147483648`   | `0`               | `2147483647`    | `4294967295`      |
| `BIGINT`    | 8     | `-2^63`         | `0`               | `2^63-1`        | `2^64-1`          |

​    

#### DECIMAIL

- 정확한 소수를 저장

```sql
DECIMAL(총자리수, 소수점뒤자리수)

-- 999.99까지 가능
DECIMAL(5, 2) 

-- 숫자의 최대크기인 소수점 앞 자리수를 초과하면 오류 발생
1534.1 >> Error

-- 소수점 뒤 자리수를 초과하면 반올림되어 저장
5.02613 >> 5.03
```

​    

#### FLOAT / DOUBLE

| 데이터 타입 | 메모리 크기 | 정밀도 문제 |
| ----------- | ----------- | ----------- |
| FLOAT       | 4 Bytes     | 7 자리이후  |
| DOUBLE      | 8 Bytes     | 15 자리이후 |

​    

### 3. Date / Time

#### DATETIME

- 날짜/시간 저장
- `1000-01-01 00:00:01 (UTC) ~ 9999-12-31 23:59:59 (UTC) ` 

#### TIMESTAMP

- 날짜/시간 저장
- 더 작은 범위의 날짜 지원하여 DATETIME보다 메모리를 덜 차지함
- `1970-01-01 00:00:01 (UTC) ~ 2038-01-19 03:14:07 (UTC) ` 

​    

---

## 3️⃣ DDL

> 기본 명령어

- 테이블 종류확인

```sql
mysql> show tables;
sqlite> .tables 
```

- 테이블 schema 조회

```sql
mysql> show columns from <테이블명> # 방법1
mysql> desc <테이블명> # 방법2
sqlite> .schema <테이블명>
```

​    

### CREATE

- 테이블 생성

```sql
create table <테이블명> (
    <컬럼명> <데이터타입> PRIMARY KEY,
);
```

> 필드 제약 조건

- NOT NULL : NULL값 입력금지
- UNIQUE : 중복값 입력금지 (NULL값은 중복 입력 가능)
- PRIMARY KEY : 테이블에서 반드시 하나만 존재 (NOT NULL + UNIQUE)
- AUTO_INCREMENT : 기본키에 1부터 자동으로 증가하는 기본 설정값을 만들어줌
- FOREIGN KEY : 외래키, 다른 테이블의 Key
- CHECK : 조건으로 설정된 값만 입력 허용
- DEFAULT : 기본 설정 값 (직접적으로 삽입되는 null값은 제어불가)

> CURRENT_TIMESTAMP : 새로운 column 생성시 첫 생성 당시 시간 저장됨
>
> ON UPDATE CURRENT_TIMESTAMP : update시 자동으로 현재시간으로 변경

```sql
CREATE TABLE 테이블명 (
  created_at TIMESTAMP default CURRENT_TIMESTAMP, 
  updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

```sql
-- 활용 예시
CREATE TABLE students(
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER DEFAULT 1 CHECK (0 < age)
);

CREATE TABLE students(
  id INTEGER AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INTEGER DEFAULT 1 CHECK (0 < age)
  PRIMARY KEY(id)
);
```

​    

### ALTER

1. 테이블 이름 변경 (`rename to`)

```sql
ALTER TABLE <변경전 테이블명>
RENAME TO <변경후 테이블명>;
```

2. 새로운 컬럼 추가 (`add column`)

```sql
ALTER TABLE <테이블명>
ADD COLUMN <새로 추가할 컬럼명>
```

3. 컬럼명 이름 수정 (`rename column`) 

```sql
ALTER TABLE <테이블명>
RENAME COLUMN <변경전 컬럼명> TO <변경후 컬럼명>
```

4. 컬럼 삭제 (`drop column`)

```sql
ALTER TABLE <테이블명>
DROP COLUMN <삭제할 컬럼명>
```

​    

### DROP

- 테이블 삭제

```sql
DROP TABLE <테이블명>; 
```

