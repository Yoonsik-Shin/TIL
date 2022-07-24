# Phase8 : [기본 수학 2](https://www.acmicpc.net/step/10)



## ▶️시도한 문제

| Try_Date        | Number | Title                                                   | Solve_Date                 | My_Solve               |
| --------------- | ------ | ------------------------------------------------------- | -------------------------- | ---------------------- |
| 2022.07.12 (화) | 1978   | [소수 찾기](https://www.acmicpc.net/problem/1978)       | 🟢 / 2022.07.12 (수)        | [1978.py](./1978.py)   |
| 2022.07.12 (화) | 2581   | [소수](https://www.acmicpc.net/problem/2581)            | 🟢 / 2022.07.12 (수)        | [2581.py](./2581.py)   |
| 2022.07.12 (화) | 11653  | [소인수분해](https://www.acmicpc.net/problem/11653)     | 😭 구글링 / 2022.07.14 (목) | [11653.py](./11653.py) |
| 2022.07.12 (화) | 1929   | [소수 구하기](https://www.acmicpc.net/problem/1929)     | 😭 구글링 / 2022.07.14 (목) | [1929.py](./1929.py)   |
| 2022.07.23 (일) | 4948   | [베르트랑 공준](https://www.acmicpc.net/problem/4948)   | 🟢 / 2022.07.23 (일)        | [4948.py](./4948.py)   |
| 2022.07.23 (일) | 9020   | [골드바흐의 추측](https://www.acmicpc.net/problem/9020) | 🟢 / 2022.07.23 (일)        | [9020.py](./9020.py)   |



## 💫다시 풀어볼만한 문제

| Number | Title                                                   |
| ------ | ------------------------------------------------------- |
| 4948   | [베르트랑 공준](https://www.acmicpc.net/problem/4948)   |
| 9020   | [골드바흐의 추측](https://www.acmicpc.net/problem/9020) |



## 💦여러번 시도한 문제

| Number | Title                                               | Solve    |
| ------ | --------------------------------------------------- | -------- |
| 1978   | [소수 찾기](https://www.acmicpc.net/problem/1978)   | 🟢        |
| 2581   | [소수](https://www.acmicpc.net/problem/2581)        | 🟢        |
| 11653  | [소인수분해](https://www.acmicpc.net/problem/11653) | 😭 구글링 |
| 1929   | [소수 구하기](https://www.acmicpc.net/problem/1929) | 😭 구글링 |



## 📑개념 정리 

```bash
# 소수 관련 내용 구글링
새로 알게된 개념
1. 소인수분해 아이디어
2. 시간복잡도 고려한 코딩
```

```python
# 소인수분해 아이디어
import math

N = int(input())    # 나누어지는 수
d = 2               # 나누는 수
sqrt = int(math.sqrt(N)) # 나누어지는 수의 제곱근


while d <= sqrt:
    if N % d != 0:  # 나누어 떨어지지 않으면
        d += 1      # 나누는 수 1 증가
    else:           # 나누어 떨어지면
        print(d)    # 소인수니까 출력하고
        N //= d     # 나누어지는 수도 갱신

# 제곱근까지 나누어떨어지지 않으면, 소수이므로 그대로 출력
if N > 1:
    print(N)
```

```python
# 소수 구하기 아이디어 - 1
number = int(input())
n = map(int, input().split())
sosu = 0

for i in n:
    error = 0 
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
                sosu += 1
print(sosu)
```

```python
# 소수 구하기 아이디어 - 2 : 에라토스테네스의 체
M, N = map(int,input().split())
a = [False, False] + [True]*(N-1)  ◀️◀️
lst = []

for i in range(2, N+1):
    if a[i]:
        lst.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

for k in lst:
    if k >= M:
        print(k)
```

![Sieve_of_Eratosthenes_animation](README.assets/Sieve_of_Eratosthenes_animation.gif)
