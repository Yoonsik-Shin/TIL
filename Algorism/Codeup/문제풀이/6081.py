var = input()

for i in range(1,16):
    print(f'{var}*{hex(i)[2:].upper()}={hex(int(var,16)*i)[2:].upper()}')