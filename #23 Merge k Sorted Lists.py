'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def Printself(n: ListNode):
    node = n
    while node != None:
        print(node.val, "-->")
        node = node.next

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        result = lists
        current = []
        while len(result) != 1:
            current = []
            for i in range(int((len(result) + 1)/2)):
                mergedList = None
                if i * 2 + 1 > len(result) - 1:
                    mergedList = self.mergeTwoLists(result[i*2], None)
                else:
                    mergedList = self.mergeTwoLists(result[i*2], result[i*2+1])
                current.append(mergedList)
            result = current
        return result[0]
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        p1 = list1
        p2 = list2
        result = None
        if list1.val > list2.val:
            result = list2
            p2 = p2.next
        else:
            result = list1
            p1 = p1.next

        current = result
        result.next = None
        while p1 != None or p2 != None:
            if p1 != None and p2 != None:
                if p1.val > p2.val:
                    current.next = p2
                    p2 = p2.next
                else:
                    current.next = p1
                    p1 = p1.next
            elif p1 != None:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        return result

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(4)
    l3 = ListNode(5)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(1)
    l5 = ListNode(3)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6

    l7 = ListNode(2)
    l8 = ListNode(6)
    l7.next = l8

    solution = Solution()
    node = solution.mergeKLists([l1, l4, l7])
    Printself(node)
