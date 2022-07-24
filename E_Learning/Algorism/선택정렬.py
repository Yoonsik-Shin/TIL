'''
선택정렬
> 처리되지 않은 데이터중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
> 이중반복문 이용
> 시간복잡도 : N + (N-1) + (N-2) + ... + 2 = (N**2+N-2)/2
> 빅오표기법 : O(N**2)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):  # i는 가장 작은 데이터와 자리가 바뀔 인덱스를 의미
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:  # 만약 현재 작은 데이터보다 더 작은 데이터가 있다면
            min_index = j    # 그 인덱스값을 min_index에 담아준다.
    
    array[i], array[min_index] = array[min_index], array[i]  # 스와프 연산

print(array)