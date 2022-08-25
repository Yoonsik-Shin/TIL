# Phase14 : [정수론 및 조합론](https://www.acmicpc.net/step/18)



## ▶️시도한 문제

| Try_Date        | Number | Title                                                        | Solve_Date           | My_Solve               |
| --------------- | ------ | ------------------------------------------------------------ | -------------------- | ---------------------- |
| 2022.08.15 (월) | 5086   | [배수와 약수](https://www.acmicpc.net/problem/5086)          | 🟢 / 2022.08.15 (월) | [5086.py](5086.py) |
| 2022.08.17 (수) | 1037   | [약수](https://www.acmicpc.net/problem/1037)                 | 🟢 / 2022.08.17 (수) | [1037.py](1037.py) |
| 2022.08.17 (수) | 2609   | [최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609) | 🟢 / 2022.08.17 (수) | [2609.py](2609.py) |
| 2022.08.19 (금) | 1934   | [최소공배수](https://www.acmicpc.net/problem/1934)           | 🟢 / 2022.08.19 (금) | [1934.py](1934.py) |
| 2022.08.21 (토) | 2981   | [검문](https://www.acmicpc.net/problem/2981)                 | 🔴 | [2981.py](2981.py) |
| 2022.08.20 (토) | 3036   | [링](https://www.acmicpc.net/problem/3036)                   | 🟢 / 2022.08.20 (토) | [3036.py](3036.py) |
| 2022.08.21 (토) | 11050  | [이항 계수 1](https://www.acmicpc.net/problem/11050)         | 🟢 / 2022.08.21 (토) | [11050.py](11050.py) |
| 2022.08.21 (토) | 11051  | [이항 계수 2](https://www.acmicpc.net/problem/11051)         | 🟢 / 2022.08.21 (토) | [11051.py](11051.py) |
| 2022.08.21 (토) | 1010   | [다리 놓기](https://www.acmicpc.net/problem/1010)            | 🟢 / 2022.08.21 (토) | [1010.py](1010.py) |
| 2022.08.21 (토) | 9375   | [패션왕 신해빈](https://www.acmicpc.net/problem/9375)        | 🟢 / 2022.08.24 (수) | [9375.py](9375.py) |
| 2022.08.21 (토) | 1676   | [팩토리얼 0의 개수](https://www.acmicpc.net/problem/1676)    | 🟢 / 2022.08.21 (토) | [1676.py](1676.py) |
| 2022.08.21 (토) | 2004   | [조합 0의 개수](https://www.acmicpc.net/problem/2004)        | 🔴 | [2004.py](2004.py) |

## 💫다시 풀어볼만한 문제

| Number | Title |
| ------ | ----- |
|        |       |



## 💦여러번 시도한 문제

| Number | Title                                                 | Solve |
| ------ | ----------------------------------------------------- | ----- |
| 2981   | [검문](https://www.acmicpc.net/problem/2981)          | 🔴     |
| 9375   | [패션왕 신해빈](https://www.acmicpc.net/problem/9375) | 🔴     |
| 2004   | [조합 0의 개수](https://www.acmicpc.net/problem/2004) | 🔴     |



## 📑개념 정리

```python
# 부동소수점
0.1 * 3 == 0.3
>> False

1.2 - 0.1 == 1.1
>> False

0.1 * 0.1 == 0.01
>> False

# 0.1의 표시값 vs 실제값
0.1 vs 0.1000000000000000055511151231257827021181583404541015625

# 부동소수점 문제해결법
# 1. decimal 모듈 활용 (❗문자열로 처리해야함)
from decimal import Decimal

Decimal('0.1') + Decimal('2.2')
>> Decimal('2.3')

Decimal('7.77') * Decimal('100')
>> Decimal('777.00')

# 2. math 모듈 활용 (True/False)
from math import isclose

print(isclose(3.315, 3.315))
>> True

# 조합 (Combination)
from itertools import combinations

print(list(combinations([1, 2, 3, 4], 2)))
>> (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
```
