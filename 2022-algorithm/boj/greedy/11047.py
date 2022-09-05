n, k = map(int, input().split())
coins = []
count = 0

for i in range(n):
    coins.append(int(input()))

for coin in coins[::-1]:
    if k == 0:
        break
    if k // coin > 0:
        count += k // coin
        k %= coin
        continue


print(count)
