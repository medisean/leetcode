'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def PrintSelf(self):
        p = self
        while p != None:
            print(p.val, "-->")
            p = p.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        while p != None and p.next != None:
            next = p.next
            p.val, next.val = next.val, p.val
            p = next.next
        return head

if __name__ == '__main__':
    head = ListNode(10)
    h1 = ListNode(11)
    # h2 = ListNode(12)
    head.next = h1
    # h1.next = h2
    solution = Solution()
    solution.swapPairs(head).PrintSelf()