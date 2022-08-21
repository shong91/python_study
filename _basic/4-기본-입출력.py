'''
입력
input(): 문자열 입력
map(): 리스트의 모든 원소에 각각 특정한 함수를 적용

readline(): 입력을 빠르게 받아야 하는 경우. 
입력 후 엔터 줄바꿈 기호를 제거하기 위해 rsstrip() 사용
'''

import sys

data = list(map(int, input().split()))
data.sort(reverse=True)
a, b, c = map(int, input().split())

data = sys.stdin.readline().rstrip()
print(data)

'''
출력
'''
print(1, end=' ')
print(2, end=' ')

answer= 10
print(f"정답은 {answer} 입니다.")
