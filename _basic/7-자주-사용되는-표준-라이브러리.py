'''
기본 내장함수
itertools: 순열, 조합
heapq: 힙 자료구조. 우선순위 큐. 최단경로 알고리즘
bisect: 이진탐색
collections: 덱, 카운터
math: 필수적인 수학적 기능. 팩토리얼, 제곱근, 최대공약수 등
'''

import math
from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


'''
내장함수
'''
result = sum([1, 2, 3, 4, 5])
min_result = min(1, 2, 3, 4)
max_result = max(6, 7, 8, 9)

result = eval("(3+5)*7")
print(result)  # 56

result = sorted([9, 1, 2, 6, 3])
reverse_result = sorted([9, 1, 2, 6, 3], reverse=True)


'''
순열과 조합
# 순열: nPr - 순서를 고려함
# 조합: nCr - 순서를 고려하지 않음
'''

# 순열
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
result = list(combinations(data, 2))
print(result)

# 중복 순열
result = list(product(data, repeat=2))
print(result)

# 중복 조합
result = list(combinations_with_replacement(data, 2))
print(result)

'''
collections
# Counter
# 반복 가능한 객체가 주어졌을 때, 내부의 원소가 몇 번씩 등장했는지 확인
'''


counter = Counter(['a', 'a', 'b', 'c', 'd', 'd', 'd'])
print(counter['a'])
print(counter['b'])
print(counter['c'])
print(counter['d'])
print(dict(counter))

'''
math
'''


def lcm(a, b):
    # 최소공배수 계산
    return a * b // math.gcd(a, b)


a = 21
b = 14

# 최대공약수 계산
print(math.gcd(a, b))
print(lcm(a, b))
