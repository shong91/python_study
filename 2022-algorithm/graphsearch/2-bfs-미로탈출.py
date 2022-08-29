'''
4 <= N, M <= 200
 
 N * M 의 미로에서  출발 (1,1) -> 탈출 (n,m) 할 때,
 이동할 최소 칸의 갯수를 구하라. 

 0 = 이동불가 
 1 = 이동가능
'''

from collections import deque

# 해결 - bfs
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어났을 시 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동불가인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))
