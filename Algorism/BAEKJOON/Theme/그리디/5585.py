pay = int(input())
rest = 1000 - pay
money_lst = [500, 100, 50, 10, 5, 1]
count = 0

while True:
  if rest == 0:
    break
  
  for i in money_lst:
    if rest // i != 0:
      count += rest // i
      rest -= i*(rest // i)
  
print(count)
