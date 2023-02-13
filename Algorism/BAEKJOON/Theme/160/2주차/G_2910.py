n, c = map(int,input().split())
m = list(map(int,input().split()))
value = {}
order = {}
order_num = 1

for i in range(n):
  if m[i] not in value:
    value[m[i]] = 1
    order[m[i]] = order_num
    order_num += 1
  else:
    value[m[i]] += 1

value = sorted(value.items(), key=lambda x: x[1] ,reverse=True)

dict_ = {}
for j in value:
  dict_[order[j[0]]] = j

for k in dict_.values():
  for _ in range(k[1]):
    print(k[0], end=' ')