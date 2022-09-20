'''
https://school.programmers.co.kr/questions/25736?question=25736

이동가능한 정점은 리스트의 형태로 재귀호출을 보낼 경우, 리스트가 완전 복제가 일어나지 않게 되면, 독립적 변수로 취급이 되지 않아 다른 곳에서 값을 바꾸면 연쇄적으로 이어져서 값이 바뀌어 최악의 상황을 초래하게 된다. 항상 배열이나 리스트의 자료형태를
값을 독립적으로 바꾸는 작업을 수행 할 때는, 무조건 복제를 하여 독립적 리스트로써 사용하도록 주의해야한다.
분명 말했습니다. 완탐문제에서는 이런 문제가 아주 많이 발생합니다. 주의합시다.

결과 변수의 최대값 갱신은 항상 양과 늑대의 수를 업데이트한 이후와 늑대의 수를 양의 수를 넘었는 지의 조건문을 탐색하는 그 중에 배치해야한다.
가끔 그런 분들이 있을 수 있는데, 당연히 wolf가 sheep의 수를 따라잡거나 초과하는 조건문에서만 결과 변수의 최댓값을 갱신하는 분이 있을 수 있다.
하지만 그렇게 되면, 모든 정점을 탐색하는 경우에 양의 수가 늑대의 수보다 많은 경우를 탐색하는 것이 불가능할 것이다. 이런 어이없는 경우가 생기지 않도록 조심하자.
'''


def dfs(x, sheep, wolf, possible):
    global info_copy, answer,  graph

    if info_copy[x] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1

    if sheep <= wolf:
        return

    possible.extend(graph[x])
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])


def solution(info, edges):
    global answer, info_copy, visited, graph
    answer = 0
    info_copy = info
    sheep, wolf = 0, 0
    graph = [[] for _ in range(len(info))]

    # 이미 지나갔던 정점은 다시 방문하더라도, 아무런 변화가 없습니다.
    # 해당 정점에 서식했던 동물이 따라오게 때문이고, 그게 게임이 끝날 때 까지 계속 따라 다니기 때문입니다.
    # 같은 정점을 다시 방문해도 결국에는, 아무런 의미가 없습니다.
    # 즉, 양방향일 필요가 없이 단방향 그래프를 통해 재귀호출하면 된다
    for a, b in edges:
        graph[a].append(b)
        # graph[b].append(a)

    dfs(0, sheep, wolf, [])

    return answer


if __name__ == '__main__':

    info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
             [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

    answer = solution(info, edges)
    print(answer)
