'''
8 * 8 의 좌표평면 상에서, 나이트가 이동할 수 있는 경우의 수 

나이트는 L 자 형태로만 이동 가능 
1. 수평으로 2칸 and 수직으로 1칸
2. 수직으로 2칸 and 수평으로 1칸

행: 1~8
렬: a~h 
'''

data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1
print(row, col)
move_plans = [(2, 1), (2, -1), (-2, 1), (-2, 2),
              (1, 2), (-1, 2), (-1, 2), (-1, -2)]
count = 0

for plan in move_plans:
    next_row = row + plan[0]
    next_col = col + plan[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1


print(count)
