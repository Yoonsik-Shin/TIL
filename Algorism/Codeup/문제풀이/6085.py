w, h, b = map(int,input().split())

print(f'{(w*h*b)/(2**23):.2f} MB')