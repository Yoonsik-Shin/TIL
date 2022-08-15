L = int(input())
word = input()
dict_alpha = {}
x = 'a'
r = 31
M = 1234567891

for _ in range(1,27):
    dict_alpha[x] = _
    x = ord(x)
    x += 1
    x = chr(x)

H = 0

for i in range(L):
    H += dict_alpha[word[i]] * (r**i) 

print(H%M)