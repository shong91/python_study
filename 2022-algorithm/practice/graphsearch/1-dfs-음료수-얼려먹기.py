'''
1 <= N, M <= 1,000 
N * M 의 얼음틀에서, 
구멍이 뚫려있는 부분 = 0 
구멍이 막혀있는 부분 = 1

구멍이 뚫려있는 부분으로 아이스크림을 얼릴 수 있다고 할 때, 
한 번에 만들 수 있는 아이스크림의 개수를 구하라. 
'''

from collections import deque


# 해답 - dfs

n, m = map(int, input().split())
array = []
count = 0
for i in range(n):
    array.append(list(map(int, input())))

print(array)


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        print(f"x: {x}, y: {y}", x, y)
        return False

    if array[x][y] == 0:
        # 방문처리
        array[x][y] = 1
        # 인접 노드 방문처리를 위해 상하좌우 위치 재귀호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(i, j)
            count += 1

print(count)
