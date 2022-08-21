from typing import List


def solution(numbers: List[int]) -> str:
    answer1 = max(numbers)
    answer2 = numbers.index(answer1)
    return "{}\n{}".format(answer1, answer2)


if __name__ == '__main__':
    numbers = [3, 29, 38, 12, 57, 74, 40, 85, 61]
    print(solution(numbers))