'''
N×M크기의 배열로 표현되는 미로
1 = 이동 가능 
0 = 이동 불가 
(1,1) -> (n,m) 으로 이동하는 최소 칸의 수 
인접한 칸으로만 이동할 수 있음
'''
# 인접한 칸으로만 이동 & 최소 칸의 수 == BFS!

from collections import deque


def bfs(x, y):
    queue = deque()
    # 큐에 넣고 방문처리
    queue.append((x, y))

    while queue:
        # 큐에서 하나 뽑고
        x, y = queue.popleft()

        # 인접한 녀석들 파악 - 상하좌우(4)
        for i in range(4):
            next_x = dx[i] + x
            next_y = dy[i] + y

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue

            if graph[next_x][next_y] == 0:
                continue

            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1

    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0

result = bfs(x, y)
print(result)
