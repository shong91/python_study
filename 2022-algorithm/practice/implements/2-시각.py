'''
00:00:00 ~ N:59:59 사이에 3이 하나라도 포함되는 모든 경우의 수 
1 <= N <= 23
'''

n = int(input())
count = 0

for i in range(n+1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
