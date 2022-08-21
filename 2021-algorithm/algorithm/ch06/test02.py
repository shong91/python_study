from typing import List
"""
문자열 뒤집기: 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하여 문자열을 뒤집어라. 
"""

def reverseString(self, s: List[str]) -> None:
    s.reverse()
    # 주의할 점!
    # [::-1] 이 정상 처리되지 않는 경우(공간 복잡도를 O(1)으로 제한하였을 경우) -> 아래와 같이 trick 사용.
    s[:] = s[::-1]