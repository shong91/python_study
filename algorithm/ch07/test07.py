from typing import List


# solve2: target -num 이 존재하는지 in 연산을 이용하여 검사
def twoSum(self, nums:List[int], target:int) -> List[int]:
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums[i+1:]:
            return nums.index(num), nums[i+1:].index(complement) + (i+1)


# solve3: 첫 번째 수를 뺀 결과 key 조회
def twoSum(self, nums:List[int], target:int) -> List[int]:
    nums_map = {}
    # key, value를 바꿔서 딕셔너리로 저장 ==> target - num 으로 두번째 수를 바로 알아낼 수 있다.
    for i, num in enumerate(nums):
        nums_map[num] = i

    # target 에서 첫 번째 수를 뺀 결과로 키를 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]


# solve4: 조회구조 개선 (하나의 for문으로 통합)
def twoSum(self, nums:List[int], target=int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i