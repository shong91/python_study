
def dfs(x, sheep, wolf):
    global answer, visited, graph
    if x >= len(visited):
        return False

    visited[x] = True
    if info[x] == 0:
        sheep += 1
    else:
        wolf += 1

    if sheep <= wolf:
        return False

    print(x, sheep,  wolf)
    for i in graph[x]:
        if not visited[i] and dfs(i, sheep, wolf):
            answer += 1
            continue
            # sheep += 1

    # 반대편 노드를 탐색해야..
    # dfs(x+1, sheep, wolf)
    return True


def solution(info, edges):
    global answer, visited, graph
    answer = 0
    sheep, wolf = 0, 0
    graph = [[]*len(info) for _ in range(len(info))]
    visited = [False]*len(info)

    for a, b in edges:
        # a, b = map(int, edge)
        graph[a].append(b)
        graph[b].append(a)

    dfs(0, sheep, wolf)

    return answer


if __name__ == '__main__':

    info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
             [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

    answer = solution(info, edges)
    print(answer)
