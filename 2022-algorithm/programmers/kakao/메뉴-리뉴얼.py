import itertools
from collections import Counter

'''
다른 사람의 풀이
'''


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(
                sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v >
                   1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]


'''
나의 풀이
'''


def solution(orders, course):
    answer = []
    # 개수마다 조합한 후 max counter 계산
    # (전체 케이스를 다 조합한 뒤에는 max counter 계산이 어려움)
    for r in course:
        temp = []
        for order in orders:
            nCr = itertools.combinations(sorted(order), r)
            temp.extend(list(nCr))

        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer.extend([''.join(x) for x in counter if counter[x]
                          == max(counter.values())])

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
answer = solution(orders, course)
print(answer)
