'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printSelf(self):
        l = self
        while l != None:
            print(l.val)
            l = l.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        result = None
        current = None
        p1 = l1
        p2 = l2
        if l1.val < l2.val:
            result = l1
            current = l1
            p1 = l1.next
        else:
            result = l2
            current = l2
            p2 = l2.next
        
        while p1 != None or p2 != None:
            if p1 != None and p2 != None:
                if p1.val <= p2.val:
                    current.next = p1
                    p1 = p1.next
                else:
                    current.next = p2
                    p2 = p2.next
            elif p1 != None:
                current.next = p1
                p1 = p1.next
            elif p2 != None:
                current.next = p2
                p2 = p2.next
            current = current.next
        return result

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(5)

    l4 = ListNode(2)
    l5 = ListNode(4)

    l1.next = l2
    l2.next = l3

    l4.next = l5
    
    solution = Solution()
    print(solution.mergeTwoLists(None, l4).printSelf())