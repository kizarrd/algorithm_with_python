# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(val=1)
b = ListNode(val=2)
c = ListNode(val=3)
b.next = c
d = ListNode(val=4)
c.next = d

prev = a
node = b
# 1(prev)   2(node) --> 3 --> 4 인 상황. (a와 b는 link되어 있지 않음.)

prev, node.next, node = node, prev, node.next
# prev, node.next = node, prev

# node, prev, node.next = node.next, node, prev
# prev, node, node.next = node, node.next, prev

print('prev: ', prev.val)
print('prev.next: ', prev.next.val)
print('node: ', node.val)
print('node.next: ', node.next.val)

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         node = head
#         prev = None
        
#         while node:
#             prev, node.next, node = node, prev, node.next
            
#         return head