'''
연구소
연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

'''

# 어디에 벽을 세워야 최댓값이 나올지는 알 수 없기 때문에 벽을 세울 수 있는 모든 경우의 수에 대해 수행해봐야 한다.
# 따라서, (1, 1) 칸 부터 (n, m)칸 까지 중 빈칸을 순서대로 하나씩 3개 선택하여 벽을 세우고 BFS를 수행한 후 벽을 지우고
# 그 다음칸에 대해 다시 벽을 세우고 BFS를 수행하고 벽을 지우는 방식 (백트래킹)을 반복해야 한다.
# 이렇게 진행하면서 최댓값을 저장한 후, 모든 탐색이 끝난 후 최댓값을 출력하면 된다.


from collections import Counter, deque
import copy
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    # input data 에서 바이러스(2) 인 값들만 queue 에 넣는다
    for i, list in enumerate(tmp_graph):
        if 2 in list:
            queue.append((i, list.index(2)))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 1 or tmp_graph[nx][ny] == 2:
                continue
            if tmp_graph[nx][ny] == 0:
                # 방문처리하고 큐에 넣는다
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer

    flat_list = [item for elem in tmp_graph for item in elem]
    counter = Counter(flat_list)
    answer = max(answer, counter[0])


def make_wall(cnt):
    if cnt == 3:
        # 벽을 다 세웠으면 bfs 를 수행
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


# 방향 벡터 - 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
count = 0

# 벽을 세우는 함수
make_wall(0)

print(answer)
