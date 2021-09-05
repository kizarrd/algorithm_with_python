# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

c = ListNode(val=3)
b = ListNode(val=2, next=c)
a = ListNode(val=1, next=b)

print(f'[{a.val}, {a.next.val}, {a.next.next.val}]')

x = a.next
b.val = 1.5

print(x.val)

y = a
y = y.next
print("y = ", y.val)
print("a = ", a.val)