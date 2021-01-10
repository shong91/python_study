from typing import List


def reverseString(self, s: List[str]) -> None:
    s.reverse()
    # 주의할 점!
    # [::-1] 이 정상 처리되지 않는 경우(공간 복잡도를 O(1)으로 제한하였을 경우) -> 아래와 같이 trick 사용.
    s[:] = s[::-1]