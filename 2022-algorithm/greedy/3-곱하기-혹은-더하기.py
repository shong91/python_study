'''
x, + 연산자를 넣어 가장 큰 수를 만든다.
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
ex) 02984 => 0 + 2 * 9 * 8 * 4
'''
array = input()
result = int(array[0])

for i in range(1, len(array)):
    num = int(array[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
