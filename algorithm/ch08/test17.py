"""
연결 리스트를 입력받아 페어 단위로 스왑하라.
입력; 1->2->3->4
출력; 2->1->4->3

"""


# 풀이1: 구조는 그대로 유지하되, 값만 변경하기
def swapPairs(self, head):
    cur = head
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


# 풀이2: 반복 구조로 스왑
def swapPairs(self, head):
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b 가 a(head) 를 가리키도록 할당 (구조 swap)
        b = head.next
        head.next = b.next
        b.next = head

        # prev 가 b를 가리키도록 할당
        prev.next = b

        # 다음 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    return root.next


# 풀이3: 재귀 구조로 스왑
def swapPairs(self, head):
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head