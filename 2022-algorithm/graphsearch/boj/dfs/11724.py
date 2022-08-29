import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        # 방문처리
        if not visited[i]:
            dfs(i)


if __name__ == '__main__':
    # n = 정점의 개수, m = 간선의 개수
    n, m = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)
    count = 0

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for j in range(1, n+1):
        if not visited[j]:
            count += 1
            dfs(j)

    print(count)
