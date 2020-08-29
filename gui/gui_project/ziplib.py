kor = ['사과', '바나나', '오렌지']
eng = ['apple', 'banana', 'orange']

# 2개의 리스트를 합쳐줌
print(list(zip(kor, eng)))

# 합쳐진 리스트를 분리하기 (*)
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)