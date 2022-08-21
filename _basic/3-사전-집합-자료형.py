'''
리스트나 튜플은 순서가 존재 -> 인덱싱, 슬라이싱 가능
사전, 집합 자료형 -> 순서가 없으므로 인덱싱 불가. key 나 element 를 통해 O(1) 의 시간복잡도로 데이터를 조회할 수 있다. 
'''

'''
사전(딕셔너리) 자료형
키, 값의 쌍을 데이터로 가지는 자료형. 순서는 없다.
임의의 변경불가능한 자료형을 키로 사용한다.

해시테이블 -> 상수 시간(O(1)) 으로 데이터 조회 가능
'''

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys()
value_list = data.values()

if '사과' in data:
  print('exists !')

data2 = {
  '홍길동': 92, 
  '이순신': 97
}

'''
집합(set) 자료형 
중복 허용 X, 순서가 없다. 

데이터의 조회, 수정에 있어 상수시간 적용
'''

data = set([0,1,2,3,4,4,5])
print(data)

data2 = {1,1,2,3,4,4,4,5,6}
print(data2)

print(data | data2)
print(data & data2)
print(data - data2)

data.add(9)
data.update([7,8])
data.remove(2)