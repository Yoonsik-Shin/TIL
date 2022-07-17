# 다시 볼만한 개념

```python
# [6046][6047] 시프트연산자
n << 1 : 2 배
n << 2 : 2*2 배
n << 3 : 2*2*2 배

n >> 1 : 1/2 배
n >> 2 : 1/2*2 배
n >> 3 : 1/2*2*2 배

a << b : a의b승
```

```python
# [6059][6060][6061][6062] 비트연산자
~(bitwise not)  >> ~n = -n-1
&(bitwise and 연산)
|(bitwise or 연산)
^(bitwise xor 연산)
<<(bitwise left shift 연산)
>>(bitwise right shift 연산)

# -1은 11111111 11111111 111111111 11111111
```

```python
# [6063] 조건표현식 (Conditional Expression)
<true인 경우 값> if <조건> else <false인 경우 값>
```

```python
# [6081] 16진수 다루기
var = input()

for i in range(1,16):
    print(f'{var}*{hex(i)[2:].upper()}={hex(int(var,16)*i)[2:].upper()}')
```

```python
# [6092] 값들의 수 세기
lst = [2, 3, 3, 2, 3] 	# 셀 수들이 들어있는 리스트
d = []  # 수 갯수를 저장할 리스트

for i in range(n): 
    d.append(0) # 초기값 설정 >> [0,0, ..., 0] >> d[0]=0, d[1]=0, ... , d[n]=0

for j in range range(len(lst)):
    d[lst[j]] += 1 	 # d[]에 1씩 추가 
```

```python
# [6095] 2차원 배열 다루기
d_v = []
d_h = []

for i in range(n):
    d_v.append(d_h)  # print(d_v) >> [ [],[],[] ]
    for j in range(n):
        d_v[i].append(0)   
        # [[0,0, ... , 0],       # d_v[0] = [0,0, ... , 0]
        #  [0,0, ... , 0],		 # d_v[0][0] = 0
        #  	    ...     ,
        #  [0,0, ... , 0]]
```

```py
