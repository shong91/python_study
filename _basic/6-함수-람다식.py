'''
함수
'''

from array import array


x = 10


def func():
    global x
    x += 1
    print(x)


def add(a, b):
    return a+b


def operator(a, b):
    add_var = a+b
    substract_var = a-b
    multiply_var = a*b
    divide_var = a // b
    return add_var, substract_var, multiply_var, divide_var


func()
print(add(2, 8))
a, b, c, d = operator(3, 7)
print(a, b, c, d)


'''
람다 표현식 
'''

print((lambda a, b: a+b)(10, 20))


def my_key(x):
    return x[1]


array = [('홍길동', 50), ('이순신', 23), ('아무개', 80)]
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))
