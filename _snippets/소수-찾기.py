import math

# 소수 찾기


def get_prime_number(number):
    # 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다.
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
