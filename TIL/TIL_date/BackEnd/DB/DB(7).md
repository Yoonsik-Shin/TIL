# DB (7)

## View

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

