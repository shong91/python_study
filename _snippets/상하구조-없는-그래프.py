'''
상하구조가 없는 그래프 형태를 리스트에 담는다. 
리스트의 인덱스(루트 노드) : 리스트의 값(연결된 노드) 의 형태로 구성한다.
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# 1 -> 2,5 에 연결
# 2 -> 1,3,5 에 연결
...

인덱스 0 부터 시작할 경우 처리가 복잡하므로, 
그래프와 방문여부를 n+1 개 배열로 생성하고, 인덱스 1부터 값을 삽입한다.
(인덱스 0 은 빈 배열로 두는 것이 생각하기 쉽다.)
'''

# input data snippet
n = int(input())
nodes = int(input())
graph = [[False]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(nodes):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
