# DB (2)

​    

## DB 다루기

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

## DDL

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

