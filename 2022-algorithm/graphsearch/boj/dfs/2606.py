'''
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 감염되는 컴퓨터의 수를 구하라.
'''

# 연결된 모든 노드 == DFS 가 더 편함!
# 인덱스 0 을 처리하기 까다로우므로, 그냥 n+1 개의 배열을 만들고, 1부터 채우는 방식 사용.

count = 0


def dfs(v):
    global count
    # 최상단 노드를 방문처리
    visited[v] = 1

    # 그래프를 순회하며
    for i in graph[v]:
        # 방문하지 않은 노드를 방문한다
        if visited[i] == 0:
            dfs(i)
            count += 1


n = int(input())
nodes = int(input())
# 상하구조가 없으므로 그래프 형태로 생각한다.
# index 0 은 사용하지 않기 위해 n+1 개의 배열 생성한다
#
# index (최상단 노드) : list (연결된 노드) 의 형태
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# 1 -> 2,5 에 연결
# 2 -> 1,3,5 에 연결
# 3 -> 2 에 연결
# 4 -> 7 에 연결
# 5 -> 1,2,6 에 연결
# 6 -> 5 에 연결
# 7 -> 4 에 연결
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(nodes):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(count)
print(sum(visited)-1)
