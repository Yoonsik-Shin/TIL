with open('./data/fruits.txt','r',encoding='utf-8') as f:
    fruits = f.read()
    fruits_lst = fruits.split('\n')
    lst = []
    Dict = {}
    for i in fruits_lst:
        if i not in lst:
            lst.append(i)
    for k in lst:
        Dict[k] = fruits_lst.count(k)

with open('03.txt','w',encoding='utf-8') as n:
    for i in Dict:
        answer = n.write(f'{i} {Dict[i]}\n')