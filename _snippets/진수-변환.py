# 10진수 -> n 진수 변환
def create_n_number(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


# n 진수 -> 10진수 변환
print(int('101', 2))
print(int('202', 3))
print(int('303', 4))
print(int('404', 5))
print(int('505', 6))
print(int('ACF', 16))

# 10진수 -> 2,8,16진수
print(bin(11))
print(oct(11))
print(hex(11))

# 시프트 연산 (2진수)
print(1 << 2)
print(5 >> 2)
