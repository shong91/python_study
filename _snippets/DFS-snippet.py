
'''
dfs snippet
'''


def dfs(v):
    # 최상단 노드를 방문처리
    visited[v] = True

    # 그래프를 순회하며
    for i in graph[v]:
        # 방문하지 않은 노드를 방문한다
        if not visited[i]:
            dfs(i)


if __name__ == '__main__':
    n = int(input())
    nodes = int(input())
    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)

    for i in range(nodes):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)
    print(count)
    print(sum(visited)-1)
