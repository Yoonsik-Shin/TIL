'''
삽입정렬
> 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
> 구현 난이도가 높은 편이지만, 일반적으로 선택정렬보다 더 효율적으로 동작
> 이중반복문
> 시간복잡도 O(N**2)
> 현재 리스트의 데이터가 거의 정렬되어 있는 경우 매우 빠르게 동작
> 최선의 경우 O(N)의 시간복잡도를 가짐
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):     # 두번째 인덱스부터 시작
    for j in range(i, 0, -1):      # 인덱스 i부터 1까지 1씩 감소
        if array[j] < array[j-1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]  # 스와프 연산
        else:                       
            break                  # 자신보다 작은 데이터를 만나면 그 위치에서 정지

print(array)