"""
홀짝연결리스트: 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. (공간복잡도 O(1), 시간복잡도 O(n)으로 풀이하라.)
입력; 1->2->3->4->5->NULL
출력; 1->3->5->2->4->NULL
"""

# 반복 구조로 홀짝 노드 처리
def oddEvenList(self, head):
    # 예외처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head