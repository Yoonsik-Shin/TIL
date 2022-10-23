for t in range(1, int(input())+1):
    N = int(input())

    for i in range(N):
        move = 0
        lst = list(map(int,input().split()))

        if len(lst):
            speed = lst[1]
        
        if lst[0] == 1:
            move += speed
        elif lst[0] == 0:
            move += speed
        elif lst[0] == 2:
            move -= speed
    
    print(move)
