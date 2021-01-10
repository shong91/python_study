from typing import List

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