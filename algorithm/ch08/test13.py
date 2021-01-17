import collections
from typing import List, Deque
"""
연결 리스트가 팰린드롬 구조인지 판별하라. 
입력; 1-> 2-> 2-> 1
출력; true
"""


# sove1: 리스트로 변환 (164ms)
def isPalindrome(self, head) -> bool:
    q: List = []
    if not head:
        return True

    node = head

    # 연결리스트(head, -> node) 를 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# solve2: 데크 자료형 이용한 최적화 (74ms)
def isPalindrome(self, head) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# solve3(BEST): 런너 사용 (64 ms)
def isPalindrome(self, head) -> bool:
    # fast runner 와 slow runner , 2개의 포인터를 이용. 각각 같은 지점(초기값 = head) 에서 출발, fast 는 2칸씩, slow 는 한 칸씩 이동한다.
    # rev 는 역순 연결 리스트
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # fast 는 마지막 값에 도달 - 홀수 일 때. slow가 한 칸 더 이동하여야 둘 다 종료.
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev