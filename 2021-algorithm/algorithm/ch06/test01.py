from collections import deque
import collections, re

"""
01. 유효한 팰린드롬
cf) 팰린드롬: 앞 뒤가 똑같은 단어난 문장 (ex) A man, a plan, a canal : Panama
"""


# 풀이 1. 리스트로 변환 [실행시간: 304ms]
def isPalindrome(self, s: str) -> bool:
    # 전처리 : 영문자/숫자 여부를 판별하여 해당하는 문자만 list에 추가한다.
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        #  list 의 맨 앞 값과 맨 뒷 값을 비교하여 불일치할 경우 false
        if strs.pop(0) != strs.pop():
            return False
    return True


# 풀이 2. 데크 자료형을 이용한 최적화 [실행시간: 64ms]
def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언 : 성능 향상의 key!
    # list 의 pop(0) 이 O(n) 인 데 반해, deque의 popleft()는 O(1) 이기 때문
    strs: deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 풀이 3. 슬라이싱 사용 [실행시간: 34ms]
def isPanindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    # [::-1] : 문자열 뒤집기
    return s == s[::-1]