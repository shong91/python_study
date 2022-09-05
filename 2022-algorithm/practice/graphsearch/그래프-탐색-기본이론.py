'''
재귀함수 - 유클리드 호제법 
'''


from collections import deque


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))


'''
DFS - 스택 or 재귀함수
1. 탐색 시작 노드를 스택에 삽입하고 방문처리 한다. 
2-1. 스택의 최상단 노드에 방문하지 않은 인접노드가 있을 시, 그 노드를 스택에 넣고 방문처리한다. 
2-2. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다. 
3. 2번 과정을 수행할 수 없을 때 까지 반복

인접한 노드가 여러개 일 때에는, 문제의 요구사항을 확인하여야 한다. 
(ex. 방문기준: 번호가 낮은 노드부터)
'''


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')

    # 스택의 최상단 노드에 방문하지 않은 인접노드가 있을 시, 그 노드를 스택에 넣고 방문처리한다. (재귀)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 인덱스 0 은 사용하지 않음
visited = [False] * 9

dfs(graph, 1, visited)

'''
BFS - 큐
1. 탐색 시작 노드를 큐에 삽입하고 방문처리 한다. 
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다. 
3. 2번 과정을 수행할 수 없을 때 까지 반복

인접한 노드가 여러개 일 때에는, 문제의 요구사항을 확인하여야 한다. 
(ex. 방문기준: 번호가 낮은 노드부터)
'''


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        # 큐에서 노드를 꺼낸 뒤에
        v = queue.popleft()
        print(v, end='')

        # 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 인덱스 0 은 사용하지 않음
visited = [False] * 9

bfs(graph, 1, visited)
