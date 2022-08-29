
'''
리스트 컴프리헨션으로 리스트 초기화하기
'''
array = [i for i in range(10)]
print(array)

array2 = [i for i in range(20) if i % 2 == 0]
print(array2)

array3 = [i*i for i in range(1, 10)]
print(array3)

# 2차원 리스트 초기화에 효과적!
# N * M 크기의 2차원 리스트를 한번에 초기화하
# 반복 수행하되, 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_) 를 사용한다.
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# 잘못된 예시: 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식된다.
array_bad = [[0] * m] * n
