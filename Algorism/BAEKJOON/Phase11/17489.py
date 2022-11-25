N = int(input())
a = '____'
b = '라고 답변하였지.'

def f(n):

    for i in range(n):
        print(f'{a*i}"재귀함수가 뭔가요?"')
        print(f'{a*i}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{a*i}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{a*i}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    return f'{a*n}"재귀함수가 뭔가요?"\n{a*n}"재귀함수는 자기 자신을 호출하는 함수라네"'

def p(n):

    if n > 0:
        print(f'{a*n}라고 답변하였지.')
    elif n == 0:
        return b

    return p(n-1)

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
print(f(N))
print(p(N))