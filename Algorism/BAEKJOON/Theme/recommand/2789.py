restrict_word = 'CAMBRIDGE'
input_word = input()

for i in restrict_word:
    input_word = input_word.replace(i,'')

print(input_word)