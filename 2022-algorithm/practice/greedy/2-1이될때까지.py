'''
1 <= N <= 100,000
2 <= K <= 100,000
N이 1이 될 때 까지 수행해야 하는 횟수의 최소값
1. -1 을 하거나 
2. % K 를 하거나 (단, 나머지가 0일때만 가능)
'''

n, k = map(int, input().split())
count = 0

while True:
    # n이 k 로 나누어 떨어지는 수가 될 때 까지 target 설정
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += (n-1)
print(count)
