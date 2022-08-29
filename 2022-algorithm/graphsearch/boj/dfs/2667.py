'''
방문할때 같은 단지인 녀석들을 하나의 숫자로 묶고(1111, 2222, 3333)
그 숫자의 count 를 세고 싶었는데.. 
맘처럼 안되네 
'''


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    # 방문처리
    if graph[x][y] == 1:
        global count
        graph[x][y] = 0
        count += 1   # 각 단지내 집의 수 +1

        # 상하좌우 탐색 (재귀 호출)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True

    return False


if __name__ == "__main__":
    n = int(input())
    graph = []
    result = []
    total = 0  # 총 단지수
    count = 0  # 각 단지내 집의 수

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        graph.append(list(map(int, input())))

    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                result.append(count)
                total += 1
                count = 0

    result.sort()
    print(total)
    for value in result:
        print(value)
