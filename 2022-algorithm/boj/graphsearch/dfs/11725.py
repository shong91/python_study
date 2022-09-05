import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    # 방문처리
    visited[x] = True

    # 빈 배열일 때
    if not graph[x]:
        return

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            roots[i] = x


if __name__ == '__main__':
    n = int(input())
    graph = [[]*(n+1) for _ in range(n+1)]
    roots = [-1] * (n+1)
    visited = [False] * (n+1)

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)
    # for node in graph[2::]:
    #     print(node)

    for root in roots[2::]:
        print(root)
