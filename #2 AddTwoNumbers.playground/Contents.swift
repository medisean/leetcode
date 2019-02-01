import UIKit

var str = "Hello, playground"

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
