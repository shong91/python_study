"""
역순연결리스트: 연결 리스트를 뒤집어라.
입력; 1->2->3->4->5->NULL
출력: NULL->5->4->3->2->1
"""


# 재귀 이용하기
from algorithm.ch08.linkedList_practice import SingleLinkedList


def reverseList(self, head):
    def reverse(node, prev: None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# 반복 이용하기
def reverseList(self, head):
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
