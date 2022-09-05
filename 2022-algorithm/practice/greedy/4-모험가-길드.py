'''
N명의 모험가
공포도 X 인 모험가는 X 명의 모험가 길드에 들어가야 함
여행을 떠날 수 있는 그룹 수의 최댓값
'''


n = int(input())
k = list(map(int, input().split()))
count = 0
k.sort()

for i, value in enumerate(k):
    if value < len(k):
        count += 1
        del k[i:value]

print(count)


# 해설
result = 0  # 그룹 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in k:
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성 성공
    if count >= i:
        result += 1
        count = 0
