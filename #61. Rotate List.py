'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printSelf(self):
        l = self
        while l != None:
            print(l.val, ",")
            l = l.next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head

        nodes = []
        l = head
        while l != None:
            nodes.append(l)
            l = l.next
        
        if len(nodes) <= 1:
            return head
        
        if k >= len(nodes):
            k = k % len(nodes)
        
        if k == 0:
            return head
        
        start = len(nodes) - k
        if start - 1 >= 0:
            nodes[start-1].next = None

        nodes[-1].next = nodes[0]
        
        head = nodes[start]
        head.printSelf()
        
        return head

if __name__ == '__main__':
    head = ListNode(0)
    l1 = ListNode(1)
    # l2 = ListNode(2)

    head.next = l1
    # l1.next = l2

    solution = Solution()
    solution.rotateRight(head, 4)
    