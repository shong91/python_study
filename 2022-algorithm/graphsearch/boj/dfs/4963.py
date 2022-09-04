import sys
sys.setrecursionlimit(10**6)


def dfs(row, col):
    if row < 0 or row >= h or col < 0 or col >= w:
        return False

    if graph[row][col] == 1:
        graph[row][col] = 0
        for direction in directions:
            nrow = row + direction[0]
            ncol = col + direction[1]
            dfs(nrow, ncol)

        return True


if __name__ == '__main__':
    answer = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        graph = []
        count = 0
        for i in range(h):
            graph.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if dfs(i, j):
                    count += 1
        answer.append(count)

    for i in answer:
        print(i)
