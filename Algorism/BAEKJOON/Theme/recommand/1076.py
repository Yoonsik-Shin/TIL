dict_={
    'black':[0,10**0],
    'brown':[1,10**1],
    'red':[2,10**2],
    'orange':[3,10**3],
    'yellow':[4,10**4],
    'green':[5,10**5],
    'blue':[6,10**6],
    'violet':[7,10**7],
    'grey':[8,10**8],
    'white':[9,10**9],
}

input_1 = input()
input_2 = input()
input_3 = input()

ans = int(str(dict_[input_1][0]) + str(dict_[input_2][0])) * dict_[input_3][1]
print(ans)