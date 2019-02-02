import UIKit

/**
 
 You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 
 You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
 Example:
 
 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 Explanation: 342 + 465 = 807.
 
 **/

public class ListNode {
  public var val: Int
  public var next: ListNode?
  public init(_ val: Int) {
      self.val = val
      self.next = nil
  }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var currentL1Node = l1
        var currentL2Node = l2
        var resultNode: ListNode?
        var resultCurrentNode: ListNode?
        var isOutOfTen = false

        while true {
            if currentL1Node == nil && currentL2Node == nil {
                if isOutOfTen {
                    let currentNode = ListNode(1)
                    if resultNode == nil {
                        resultNode = currentNode
                        resultCurrentNode = resultNode
                    } else {
                        resultCurrentNode?.next = currentNode
                        resultCurrentNode = currentNode
                    }
                }
                break
            }
            
            let l1Value = currentL1Node?.val ?? 0
            let l2Value = currentL2Node?.val ?? 0
            let addedValue = isOutOfTen ? 1 : 0
            isOutOfTen = (l1Value + l2Value + addedValue) >= 10

            let currentNode = ListNode((l1Value + l2Value + addedValue) % 10)
            if resultNode == nil {
                resultNode = currentNode
                resultCurrentNode = resultNode
            } else {
                resultCurrentNode?.next = currentNode
                resultCurrentNode = currentNode
            }
            currentL1Node = currentL1Node?.next
            currentL2Node = currentL2Node?.next
        }
        return resultNode
    }
}
