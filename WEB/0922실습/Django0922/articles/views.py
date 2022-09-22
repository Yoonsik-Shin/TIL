from email.mime import image
from multiprocessing import context
from secrets import choice
from django.shortcuts import render

# Create your views here.
def index(request):
    import random
    menus = ['삼겹살', '햄버거', '피자', '치킨', '샤브샤브',]
    images = [
        'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg',
        'https://img.hani.co.kr/imgdb/resize/2017/0709/149948783091_20170709.JPG',
        'https://cdn.dominos.co.kr/admin/upload/goods/20200508_KdroBehI.jpg',
        'https://barunchicken.com/wp-content/uploads/2021/04/%EC%96%91%EB%85%90%EC%B9%98%ED%82%A8.jpg',
        'http://img3.tmon.kr/cdn3/deals/2019/06/18/2163991234/original_2163991234_front_19924_1560841473production.jpg',
    ]

    menu_index = menus.index(random.choice(menus))
    menu = menus[menu_index]
    image = images[menu_index]

    context = {
        'menu': menu,
        'img': image,
    }

    return render(request, "dinner.html", context)

def lotto(request):
    import random

    numbers = list(range(1, 46))
    lotto_num = []
    state = []

    for _ in range(5):
        a = random.sample(numbers, 7)
        lotto_num.append(a)
        bonus = False
        count = 0

        for i in range(7):
            if a[i] == 10:
                count+=1
                bonus = True
                continue
            if a[i] in [3, 11, 15, 29 ,35, 44]:
                count += 1

        if bonus == True:
            if count == 6:
                state.append(2)
            else:
                state.append(0)
        else:
            if count == 6:
                state.append(1)
            elif count == 5:
                state.append(3)
            elif count == 4:
                state.append(4)
            elif count == 3:
                state.append(5)
            else:
                state.append(0)

    context = {
        'number1': lotto_num[0],
        'number2': lotto_num[1],
        'number3': lotto_num[2],
        'number4': lotto_num[3],
        'number5': lotto_num[4],
        'rate1': state[0],
        'rate2': state[1],
        'rate3': state[2],
        'rate4': state[3],
        'rate5': state[4],
    }
    return render(request, "lotto.html", context)