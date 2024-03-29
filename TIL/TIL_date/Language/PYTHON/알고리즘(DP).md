# DP

- 동적계획법 (Dynamic Programing)

- 동적할당 : 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법
- 분할 정복과의 차이점
  - 둘다 최적 부분 구조를 가질 때 사용가능
  - DP는 각 부분 문제들이 서로 영향을 미치며 부분문제가 중복됨
  - 분할 정복은 동일한 부분 문제가 반복적으로 계산되지 않음



### 최적 부분 구조 (Optimal Substructure)

- 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아 큰 문제 해결

​    

### 중복되는 부분 문제 (Overlapping Subproblem)

- 동일한 작은 문제를 반복적으로 해결

​    

### 하향식 (탑다운)

- 메모이제이션 (Memoization)
- 한번 계산된 결과를 메모리 공간에 메모해놓는 기법
- 캐싱(Cashing)이라고도 불림



### 상향식 (바텀업)

- DP의 전형적인 형태
- 반복문 이용
- 결과 저장용 리스트는 DP테이블이라고 불림



### 대표 문제

#### 🚩 피보나치 수열

```python
1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ,89, ...
```

- 점화식 : `A(n) = A(n-1) + A(n-2)` `[ 초기조건 : A(1) = 1, A(2) = 1 ]`



>  재귀함수 

- 문제점 : 지수(2^n) 시간 복잡도를 가짐 (시간효율 낮음)
- 중복되는 부분 문제가 발생

```python
def fibo(x):
  if x == 1 or x == 2: return 1

	return fibo(x-1) + fibo(x-2)
```



> DP (탑다운)

- 시간복잡도 : O(n)

```python
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
  if x == 1 or x == 2: return 1  # 종료조건
	if d[x]: return d[x]  # 이미 계산한 적 있는 문제이면 그대로 반환
	d[x] = fibo(x-1) + fibo(x-2)  # 아직 계산하지 않은 문제라면 점화식에 따라 결과반환
  return d[x]
```

​    

> DP (바텀업)

```python
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째와 두 번째 피보나치 수는 1
d[1], d[2] = 1, 1

# 반복문으로 구현
for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]
```

