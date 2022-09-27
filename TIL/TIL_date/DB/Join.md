# ✍️ JOIN

- RDB의 가장 큰 장점이자 핵심 기능
- 일반적으로 레코드는 기본키(PK)나 외래키(FK)값의 관계로 결합

​    

>  [JOIN 시각화 사이트](https://sql-joins.leopard.in.ua/)

​    

## 1. INNER JOIN

- 두 테이블에 모두 일치하는 행만 반환
- INNER 생략가능
- 교집합

```sql
SELECT *
FROM 테이블1 [INNER] JOIN 테이블2
	ON 테이블1.컬럼 = 테이블2.컬럼;
```

![image-20220822174033248](Join.assets/image-20220822174033248.png)

​    

## 2. OUTER JOIN

- 동일한 값이 없는 데이터도 반환할 때 사용
- 기준되는 테이블에 따라 `LEFT`, `RIGHT`, `FULL`로 나뉨
- LEFT, RIGHT, FULL 사용시 OUTER 생략가능

```sql
SELECT *
FROM 테이블1 (LEFT / RIGHT / FULL) [OUTER] JOIN 테이블2
	ON 테이블1.컬럼 = 테이블2.컬럼;
```



- LEFT OUTER  JOIN

![image-20220822174237731](Join.assets/image-20220822174237731.png)

- RIGHT OUTER JOIN

![image-20220822174430284](Join.assets/image-20220822174430284.png)

- FULL OUTER JOIN

![image-20220822174510500](Join.assets/image-20220822174510500.png)

​    

## 3. CROSS JOIN

- 모든 가능한 경우의 수

```sql
SELECT *
FROM 테이블1 CROSS JOIN 테이블2;
```

