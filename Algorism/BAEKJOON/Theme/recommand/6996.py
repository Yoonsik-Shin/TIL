# https://www.acmicpc.net/problem/6996

T = int(input())

for _ in range(T):
    A, B = input().split()
    
    sorted_A = sorted(A)
    sorted_B = sorted(B)

    if sorted_A == sorted_B:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')