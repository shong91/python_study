from typing import List
"""
역순으로 저장된 연결 리스트의 숫자를 더하라.
입력; (2->4->3) + (5->6->4)
출력;  7->0->8
"""


# 자료형 변환: 연결 리스트 -> 문자열 -> 연결 리스트
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head):
        node, prev = head, None
        while node:
            next, node.next =  node.next, prev
            prev, node = node, next

    # 연결리스트를 파이썬 List 로 변환하기
    def toList(self, node):
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # List 를 연결 리스트로 변경하기 (->  return value)
    def toReversedLinkedList(self, result):
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        return self.toReversedLinkedList(str(resultStr))


# 전가산기 구현
def addTwoNumbers(self, l1, l2):
    root = head = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # 몫(자리올림수)와 나머지(값) 계산
        carry, val = divmod(sum+carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next