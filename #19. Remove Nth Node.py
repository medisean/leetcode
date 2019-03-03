'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def Printself(self):
        node = self
        while node != None:
            print(node.val, "-->")
            node = node.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        current = head
        while current != None:
            nodes.append(current)
            current = current.next
        target = nodes[len(nodes) - n]
        if len(nodes) - n - 1 < 0: # remove first node
            return target.next
        elif n == 1: # remove last node
            pre = nodes[len(nodes) - n - 1]
            pre.next = None
            return head
        else:
            target.next = None
            pre = nodes[len(nodes) - n - 1]
            next = nodes[len(nodes) - n + 1]
            pre.next = next
        return head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    node = solution.removeNthFromEnd(node1, 5)
    node.Printself()
    # print()