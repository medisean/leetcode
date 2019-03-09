'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        nodes = []
        p = head
        while p != None:
            nodes.append(p)
            p = p.next
        for i in range(int(len(nodes)/k)):
            for j in range(0, int(k/2)):
                nodes[i * k + j].val, nodes[(i + 1) * k - j - 1].val = nodes[(i + 1) * k - j - 1].val, nodes[i * k + j].val
        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    solution = Solution()
    solution.reverseKGroup(l1, 2).PrintSelf()