import re

#ca?e 

p = re.compile('ca.e') 


def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열만 반환
        print("m.string: ", m.string) # 입력받은 문자열을 그대로 반환
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print('매칭되지 않음.')


# m = p.match('careless')  # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search('good care') # search: 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m)

lst = p.findall('carelesscafe cake is defe') # 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# 정규식 활용법
# 1. p = re.compile('원하는 형태')
# 2-1. m = p.match('비교할 문자열')
# 2-2. m = p.search('비교할 문자열')
# 2-3. lst = p.findall('비교할 문자열') 리스트 형태로 반환

# 원하는 형태: 정규식
# . (ca.e): 하나의 문자를 의미함 ex) cafe, care, case.. not caffe
# ^ (^de): 문자열의 시작 ex) desk, destination .. not fade
# $ (se$): 문자열의 끝 ex) case, base .. not face
