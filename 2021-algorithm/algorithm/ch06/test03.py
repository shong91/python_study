from typing import List
"""
로그를 재정렬하라. 
1. 로그의 가장 앞 부분은 식별자다. 
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다. 
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로한다. 
4. 숫자 로그는 입력 순서대로 한다. 
"""


# 풀이 1: 람다와 + 연산자 이용
def reorderLogFiles(self, logs:List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 key 를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    """    
    + 연산자: 두 리스트의 값이 하나로 이어진다.
    a = [1,2,3]
    b = [4,5,6]
    print(a + b) # [1,2,3,4,5,6] 
    """
    return letters + digits