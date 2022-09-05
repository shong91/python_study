
'''
화폐의 종류(K)만큼만 반복이 수행됨
시간복잡도: O(K)
'''

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)
