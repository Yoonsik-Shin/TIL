# Phase10 : [정렬](https://www.acmicpc.net/step/9)

## ▶️시도한 문제

| Try_Date        | Number | Title                                                    | Solve_Date           | My_Solve               |
| --------------- | ------ | -------------------------------------------------------- | -------------------- | ---------------------- |
| 2022.07.17 (일) | 2750   | [수 정렬하기](https://www.acmicpc.net/problem/2750)      | 🟢 / 2022.07.17 (일) | [2750.py](./2750.py)   |
| 2022.07.18 (월) | 2751   | [수 정렬하기 2](https://www.acmicpc.net/problem/2751)    | 🟢 / 2022.07.18 (월) | [2751.py](./2751.py)   |
| 2022.07.18 (월) | 10989  | [수 정렬하기 3](https://www.acmicpc.net/problem/10989)   | 😭                   | [10989.py](./10989.py) |
| 2022.07.18 (월) | 2108   | [통계학](https://www.acmicpc.net/problem/2108)           | 🟢 / 2022.07.29 (금) | [2108.py](./2108.py)   |
| 2022.07.19 (화) | 1427   | [소트인사이드](https://www.acmicpc.net/problem/1427)     | 🟢 / 2022.07.19 (화) | [1427.py](./1427.py)   |
| 2022.07.19 (화) | 11650  | [좌표 정렬하기](https://www.acmicpc.net/problem/11650)   | 🟢 / 2022.07.19 (화) | [11650.py](./11650.py) |
| 2022.07.19 (화) | 11651  | [좌표 정렬하기 2](https://www.acmicpc.net/problem/11651) | 🟢 / 2022.07.19 (화) | [11651.py](./11651.py) |
| 2022.07.19 (화) | 1181   | [단어 정렬](https://www.acmicpc.net/problem/1181)        | 🟢 / 2022.07.19 (화) | [1181.py](./1181.py)   |
| 2022.07.19 (화) | 10814  | [나이순 정렬](https://www.acmicpc.net/problem/10814)     | 🟢 / 2022.07.22 (금) | [10814.py](./10814.py) |
| 2022.07.19 (화) | 18870  | [좌표 압축](https://www.acmicpc.net/problem/18870)       | 😭 / 2022.07.29 (금) | [18870.py](./18870.py) |
| 2022.08.14 (일) | 25305  | [커트라인](https://www.acmicpc.net/problem/25305)        | 🟢 / 2022.08.14 (일) | [25305.py](./25305.py) |

## 💫다시 풀어볼만한 문제

| Number | Title |
| ------ | ----- |
|        |       |

## 💦여러번 시도한 문제

| Number | Title                                                  | Solve |
| ------ | ------------------------------------------------------ | ----- |
| 10989  | [수 정렬하기 3](https://www.acmicpc.net/problem/10989) | 😭    |
| 2108   | [통계학](https://www.acmicpc.net/problem/2108)         | 🟢    |
| 10814  | [나이순 정렬](https://www.acmicpc.net/problem/10814)   | 🟢    |
| 18870  | [좌표 압축](https://www.acmicpc.net/problem/18870)     | 😭    |

## 📑개념 정리

```python
# 람다함수
lambda arg : result

def function(arg):
    return result
```

```python
# sort 메소드 매개변수
students = [
    ['yoon', 27]
    ['shin', 25]
    ['sik', 21]
]

lst.sort([key = lambda x:x[0],x[1]] , [reverse = False])
- key = lambda x:x[0,1,...]: 키를 기준으로 정렬 // 내림차순 : -x[0]
- reverse = True : 내림차순 / (기본값) reverse = False : 오름차순

# sorted함수는 리스트뿐만 아니라, 튜플, 딕셔너리, Str에서도 사용가능하다.
- 정렬기준 : 아스키 코드
- 대문자 >> 소문자
```

```python
# map함수
map(함수, 반복가능한것)
반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를 map object로 반환한다.
```

```python
❗❗정렬하기 전에 원하는 정렬기준이 문자열인지 숫자인지 꼭 확인❗❗
```

```python
# 선택정렬

```
