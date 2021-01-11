from typing import List
"""
배열을 입력받아 output[i] 가 자신을 제외하 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. (단, 나눗셈을 하지 않고 풀이하라)
입력; [1,2,3,4]
출력; [24,12,8,6]

"""


def productExceptSelf(self, nums:List[int]) -> List[int]:
    result = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        result.append(p)
        p = p * nums[i]
    # result = [1, 1, 2, 6]

    p = 1

    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0-1, -1):
        result[i] = result[i] * p
        p = p * nums[i]

    return result