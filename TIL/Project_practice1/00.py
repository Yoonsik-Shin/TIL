with open('00.txt', 'w', encoding='utf-8') as f:
    a = f.write('3회차 신윤식\nHello, Python!\n')
    for i in range(1,6):
        a = f.write(f'{i}일차 파이썬 공부 중\n')