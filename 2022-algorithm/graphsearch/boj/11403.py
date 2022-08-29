'''
플로이드 와샬 알고리즘은 모든 정점에 대한 경로를 계산하는 알고리즘이다.
 
플로이드 와샬 알고리즘을 사용하여 어느 한 곳에 들려 다른 곳으로 가는 길이 존재한다면 그 값을 체킹해준다.
 
그리고 그 그래프를 출력하면 된다.
'''
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().split())))

    # 플로이드 워셜 알고리즘(Floyd Warshall Algorithm) 이용
    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    for i in range(0, N):
        _str = ""
        for j in range(0, N):
            _str += str(graph[i][j]) + " "
        print(_str)
