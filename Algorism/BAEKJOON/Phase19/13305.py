N = int(input())
road_meter = list(map(int,input().split()))
oil_price = list(map(int,input().split()))

first_price = road_meter[0] * oil_price[0]
total_value = first_price
min_value = oil_price[0]

for i in range(1, N-1):
    if oil_price[i] < min_value:
        min_value = oil_price[i]
    total_value += min_value * road_meter[i]

print(total_value)