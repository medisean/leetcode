import UIKit

/*
 Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
 
 Example 1:
 
 Input: 121
 Output: true
 Example 2:
 
 Input: -121
 Output: false
 Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
 Example 3:
 
 Input: 10
 Output: false
 Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 */

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard x >= 0 else {
            return false
        }
        let s = String(x)
        for index in 0..<s.count/2 {
            let firstStart = s.index(s.startIndex, offsetBy: index)
            let firstEnd = s.index(s.startIndex, offsetBy: index)
            
            let secondStart = s.index(s.startIndex, offsetBy: s.count-index-1)
            let secondEnd = s.index(s.startIndex, offsetBy: s.count-index-1)

            if s[firstStart...firstEnd] != s[secondStart...secondEnd] {
                return false
            }
        }
        return true
    }
}

let solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(0))

