from collections import Counter, deque


def bfs(graph, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                continue


if __name__ == '__main__':
    n = int(input())
    graph = []
    graph_rg = []  # 적록색약용
    visited = []
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        inputs = input()
        graph.append(list(inputs))
        graph_rg.append(list(inputs.replace('R', 'G')))

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 방문하지 않았으면 bfs 수행
            if not visited[i][j]:
                bfs(graph, i, j)
                count += 1
    print(count)

    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 방문하지 않았으면 bfs 수행

            if not visited[i][j]:
                bfs(graph_rg, i, j)
                count += 1

    print(count)
