from typing import List
"""
n개의 페어를 이용한 min(a,b) 의 합으로 만들 수 있는 가장 큰 수를 출력하라. 
입력; [1,4,3,2]
출력; 4
"""


# solve1: 오름차순/내림차순 풀이
def arrayPartition(self, nums:List[int]) -> int:
    sum = 0
    pair = [] # min(a,b) 의 페어를 담을 리스트. ex) min(1,4) = 1
    nums.sort() # sort 하여 항상 최대 min() 페어를 유지할 수 있도록 함

    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            sum += min(pair)
            pair = [] # sum 후 pair 초기화
    return sum


# solve2: 짝수번째 값 계산 => 정렬된 상태에서는 항상 짝수 번째에 작은 값이 위치한다. (0부터 시작)
def arrayPartition(self, nums:List[int]) -> int:
    sum = 0
    nums.sort()

    for i, num in enumerate(nums):
        if i % 2 == 0:
            sum += num
    return sum


# solve3: 파이써닉한 방식: 슬라이싱하여 짝수번째 값 계산
def arrayPartition(self, nums:List[int]) -> int:
    return sum(sorted(nums)[::2])
