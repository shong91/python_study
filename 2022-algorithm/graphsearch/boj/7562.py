from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] += 1

    while queue:
        x, y = queue.popleft()

        if x == target_x and y == target_y:
            break

        for move_plan in move_plans:
            nx = x + move_plan[0]
            ny = y + move_plan[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[x][y]


if __name__ == '__main__':
    move_plans = [(2, 1), (2, -1), (-2, 1), (-2, 2),
                  (1, 2), (-1, 2), (-1, 2), (-1, -2)]
    testcase = int(input())
    graph = []
    inputs = []
    for i in range(testcase):
        n = int(input())
        x, y = map(int, input().split())
        target_x, target_y = map(int, input().split())
        for i in range(n):
            graph = [[0]*(n) for _ in range(n)]

        inputs.append((n, x, y, target_x, target_y, graph))

    for i in range(testcase):
        n, x, y, target_x, target_y, graph = inputs[i]
        count = bfs(x, y)
        print(count-1)
