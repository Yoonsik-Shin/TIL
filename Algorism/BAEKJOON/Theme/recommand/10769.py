# https://www.acmicpc.net/problem/10769

happy = ':-)'
sad = ':-('

sentence = input()
sentence = sentence.replace(happy,'@')
sentence = sentence.replace(sad,'#')

happy_count = sentence.count('@')
sad_count = sentence.count('#')

if happy_count > sad_count:
    print('happy')
elif happy_count < sad_count:
    print('sad')
elif  happy_count == sad_count and happy_count != 0:
    print('unsure')
else:
    print('none')