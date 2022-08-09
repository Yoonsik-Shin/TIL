R, C = map(int, input().split())

matrix = [[0] * C  for _ in range(R)]
exam = []

dr = [0, 1, 1, 1, 0, -1, -1, -1] # 우 > 우하 > 하 까지만 생각
dc = [1, 1, 0, -1, -1, -1, 0, 1] 

destroy_0, destroy_1, destroy_2, destroy_3, destroy_4 = 0, 0, 0 ,0 ,0


for _ in range(R):
    exam.append(input())

for row in range(R-1): # 2x2를 봐야함으로 인덱스 R - 2 + 1, C - 2 + 1
    for col in range(C-1):
        a = 0 # 차 안부수고 주차가능한 자리수 
        if exam[row][col] == '.': # .을 기준으로 탐색 (한칸은 차 안부수고 배치 가능)
            for i in range(3): # 우 > 우하 > 하 까지만 생각
                ny = row + dr[i]
                nx = col + dc[i]

                if 0 <= ny < R and 0 <= nx < C:
                    if exam[ny][nx] == '#': # 건물일때는 어떻게든 주차불가능 (break)
                        a = -1 # 차 안부수고 주차가능한 자리수 -1로 불가능함을 표시
                        break
                    elif exam[ny][nx] == '.': # .일때는 차 안부수고 주차 가능하므로
                        a += 1  # 차 안부수고 주차가능한 자리수 하나 추가
                
            if a == 3:  # 처음있는 자리 포함하면 차 안부수고 온전히 2*2 주차가능
                destroy_0 += 1  
            elif a == 2:
                destroy_1 += 1  # 처음있는 자리 포함하면 차 1나부수면 2*2 주차가능
            elif a == 1:
                destroy_2 += 1  # 처음있는 자리 포함하면 차 2개부수면 2*2 주차가능
            elif a == 0:
                destroy_3 += 1  # 처음있는 자리 포함하면 차 3개부수면 2*2 주차가능

        elif exam[row][col] == 'X': # X을 기준으로 탐색 (한칸은 무조건 차부수고 배치)

            for i in range(3):
                ny = row + dr[i]
                nx = col + dc[i]

                if 0 <= ny < R and 0 <= nx < C:
                    if exam[ny][nx] == '#':
                        a = -1
                        break
                    elif exam[ny][nx] == '.':
                        a += 1
                
            if a == 3: # 처음 한 자리만 차 부수면 2*2 주차가능(총 1개)
                destroy_1 += 1
            elif a == 2:    # 처음 한 자리와 1개 추가로 부수면(총 2개) 2*2 주차가능
                destroy_2 += 1
            elif a == 1:    # 처음 한 자리와 2개 추가로 부수면(총 3개) 2*2 주차가능
                destroy_3 += 1
            elif a == 0:    # 처음 한 자리와 3개 추가로 부수면(총 4개) 2*2 주차가능
                destroy_4 += 1

print(destroy_0)
print(destroy_1)
print(destroy_2)
print(destroy_3)
print(destroy_4)