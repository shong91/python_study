# 10진수를 16진수/8진수로 변환
a = input()
n = int(a)
print('%x' % n)
print('%X' % n)

a = input()
n = int(a, 16)
print('%o' % n)

# 영문자를 10진수로 변환
n = ord(input())
print(n)

# 소수점
a = input()
a = float(a)
print(format(a, ".2f"))

# 다음 문자 출력하기
n = input()
print(chr(n+1))

# 비트연산자
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)

n = 10
print(n << 1)  # 10을 2(2**1)배 한 값인 20 이 출력된다.
print(n >> 1)  # 10을 반으로 나눈 값인 5 가 출력된다.
print(n << 2)  # 10을 4(2**2)배 한 값인 40 이 출력된다.
print(n >> 2)  # 10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 정수 10의 2진수 표현은 ... 1010 이다.
# 10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
# 10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.

# 정수 2개(a, b)를 입력받아 a를 2**b배 곱한 값으로 출력해보자.
a = int(input())
b = int(input())
print(a << b)
