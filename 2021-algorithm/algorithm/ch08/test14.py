"""
정렬되어 있는 두 연결 리스트를 합쳐라.
입력; 1->2->4, 1->3->4
출력; 1->1->2->3->4->4
"""


# 재귀 구조로 연결
def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val) :
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1,next, l2)
    return l1
