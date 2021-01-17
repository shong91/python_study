"""
역순 연결 리스트: 인덱스 m에서 n까지를 역순으로 만들어라. m은 1부터 시작한다.
입력; 1->2->3->4->5->NULL. m=2, n=4
출력; 1->4->3->2->5->NULL
"""

def reverseBetween(self, head, m:int, n:int):
    if not head or m == n:
        return head
    root = start = ListNode(None)
    root.next = head

    # start, end
    for _ in range(m-1):
        start = start.next
    end = start.next

    # 뒤집기
    for _ in range(n-m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next

