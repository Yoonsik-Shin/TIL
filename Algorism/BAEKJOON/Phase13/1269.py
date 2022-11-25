A, B = map(int,input().split())
lst_A = set(map(int,input().split()))
lst_B = set(map(int,input().split()))

print(len(lst_A-lst_B)+len(lst_B-lst_A))