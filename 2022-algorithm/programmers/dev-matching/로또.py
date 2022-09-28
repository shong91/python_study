

def solution(lottos, win_nums):
    answer = [0, 6, 5, 4, 3, 2, 1]

    min = 0
    zero = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            min += 1

    max = min + zero
    if min <= 1:
        min = 1
    if max <= 1:
        max = 1

    return [answer[max], answer[min]]


lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]
answer = solution(lottos, win_nums)
print(answer)
