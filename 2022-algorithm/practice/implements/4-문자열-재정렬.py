'''
알파벳 오름차순 + 숫자(0~9) 더한 값 

'''

input_data = input()
list = []
numeric_result = 0

for input in input_data:
    if input in '0123456789':
        numeric_result += int(input)
    else:
        list.append(input)

print(''.join(list), numeric_result, sep='')


# 해답
for input in input_data:
    if input.isalpha():
        list.append(input)
    else:
        numeric_result += int(input)

list.sort()

if numeric_result != 0:
    list.append(str(numeric_result))

print(''.join(list))
