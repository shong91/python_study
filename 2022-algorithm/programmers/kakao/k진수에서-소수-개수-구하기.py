import math


# 10진수 -> n 진수 변환
def create_n_number(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


# 소수 찾기
def get_prime_number(number):
    # 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다.
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    n_number = create_n_number(n, k)
    numbers = n_number.split('0')
    for number in numbers:
        if len(number) > 0 and number != '1' and get_prime_number(int(number)):
            answer += 1

    return answer


answer = solution(110011, 10)
print(answer)
