with open('./data/fruits.txt','r',encoding='utf-8') as f:
    fruits = f.readlines()

with open('01.txt','w',encoding='utf-8') as f:
    fruits = f.write(f'{len(fruits)}')