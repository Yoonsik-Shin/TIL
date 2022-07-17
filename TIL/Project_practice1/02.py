with open('./data/fruits.txt','r',encoding='utf-8') as f:
    fruits = f.read()      
    fruits_lst = fruits.split('\n')
    # print(fruits_lst)
    ans_lst = []
    for i in fruits_lst:
        if i[-5:] == 'berry':
            ans_lst.append(i)
    ans = list(set(ans_lst))
for j in ans:
    print(j)

with open('02.txt','w',encoding='utf-8') as g:
    answer = g.write(f'{len(ans)}\n')
    for i in range(len(ans)):
        answer = g.write(f'{ans[i]}\n')



'''
Juniper berry
Salal berry
Goji berry
'''







