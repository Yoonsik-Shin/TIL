S, K, H = map(int,input().split())

univ_dict = {
    'Soongsil' : S,
    'Korea' : K,
    'Hanyang' : H
}

univ_sort = sorted(univ_dict.items(), key=lambda x:x[1])

if S+K+H >= 100:
    print('OK')
else:
    print(univ_sort[0][0])