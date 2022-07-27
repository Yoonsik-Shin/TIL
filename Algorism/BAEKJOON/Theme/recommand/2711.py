T = int(input())

for i in range(T):
    x, y = input().split()
    wrong_word_index = int(x)-1
    corret_word = y[:wrong_word_index] + y[wrong_word_index+1:]

    print(corret_word)