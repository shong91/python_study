'''
N * N 크기의 정사각형 공간에서, 상하좌우 방향으로 이동시킬 수 있다. 
좌측상단의 좌표는 (1,1)
1 <= N <= 100
1 <= 이동횟수 <= 100

'''

n = int(input())
x, y = 1, 1
plans = input().split()

# L R U D
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
