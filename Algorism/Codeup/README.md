# 다시 볼만한 개념

```python
# [6059] 조건표현식 (Conditional Expression)
<true인 경우 값> if <조건> else <false인 경우 값>
```

```python
# [6081] 16진수 다루기

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

