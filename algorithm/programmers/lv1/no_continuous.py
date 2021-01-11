from typing import List
"""
[같은 숫자는 싫어]
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
"""


def solution(arr:List[int]) -> List[int]:
    answer = []
    for num in arr:
        if [num] != answer[-1:]:
            answer.append(num)
    return answer


# 테스트 실행
if __name__ == '__main__':
    print(solution([1, 3, 3, 3, 0, 3]))
