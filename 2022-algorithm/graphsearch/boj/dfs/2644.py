def dfs(x):
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            dfs(i)


if __name__ == '__main__':
    n = int(input())
    x, y = map(int, input().split())
    m = int(input())
    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [-1] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited[x] = 0
    dfs(x)
    print(visited[y])
