from difflib import context_diff
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def OddEven(request, number):
    choose = ""
    if number % 2 == 0:
        choose = "짝수"
    else:
        choose = "홀수"
    context = {"number": number, "choose": choose}
    return render(request, "OddEven.html", context)


def calculate(request, number1, number2):
    context = {
        "number1": number1,
        "number2": number2,
        "sum": number1 + number2,
        "sub": number1 - number2,
        "multi": number1 * number2,
        "div": number1 // number2,
    }
    return render(request, "calculate.html", context)


def previous(request):

    return render(request, "previous.html")


def check(request):
    import random

    pre = ["a", "b", "c", "d", "e"]
    pre_choice = random.choice(pre)

    context = {"name": request.GET.get("name"), "pre": pre_choice}
    return render(request, "check.html", context)


def lorem(request):

    return render(request, "lorem.html")


def lorem_made(request):
    import random

    p = int(request.GET.get("p_count"))
    w = int(request.GET.get("w_count"))

    w_list = []
    random_lists = ["a", "b", "c", "d", "e", "f", "g"]

    for j in range(w):
        p_list = []
        for i in range(p):
            p_list.append(random.choice(random_lists))
        w_list.append(p_list)

    context = {
        "w_list": w_list,
    }
    return render(request, "lorem_made.html", context)
