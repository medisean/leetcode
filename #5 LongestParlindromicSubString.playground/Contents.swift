import UIKit

/**
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
 
 Example 1:
 
 Input: "babad"
 Output: "bab"
 Note: "aba" is also a valid answer.
 Example 2:
 
 Input: "cbbd"
 Output: "bb"
 
 找回最长回文串r，假设回文串长度为n, 那么其中第 i 个字符 r[n-1-i] = r[i] （0<=i<n）
 思路：因为是回文串，那么可以简化一下：
      如果长度为 3， 共有 2 + 1 = 3 种情况
      如果长度为 4， 共有 3 + 2 + 1 = 6 种情况
      如果长度为 5， 共有 4 + 3 + 2 + 1 = 10 种情况
      如果长度为 n, 共有 1 + 2 + ... (n-1) 种情况 （n > 3)
      根据学过的知识，那么共有 n * (n-1) / 2 种情况，如果遍历的话那么显然算法的复杂度为 O（n*n)
      根据策略的优化，如果 有一个 i 长度的回文子串，那么就不需要再遍历 i - 1 这种情况了，可以减少复杂度，但最坏的情况仍是 O（n*n)
 
 c
 cb
 bb cbb
 bd bbd cbbd
 
 
 **/

class Solution {
    func longestPalindrome(_ s: String) -> String {
        var t = "$#"
        for c in s {
            t.append(c)
            t.append("#")
        }
        
        var mx = 0
        var id = 0
        var resLen = 0
        var resCenter = 0
        var p: [Int] = [t.count]

        for (index, value) in t.enumerated() {
            var i = index + 1
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1
            
            while t[i + p[i]] == t[i - p[i]] {
                p[i] + = 1
            }
            if mx < i + p[i] {
                mx = i + p[i]
                id = i
            }
            if resLen < p[i] {
                resLen = p[i]
                resCenter = i
            }
        }
        let str = s as NSString
        return str.substring(with: NSRange(location: (resCenter - resLen) / 2, length: resLen - 1))
    }
}

let solution = Solution()
print(solution.longestPalindrome("babad"))

//print(solution.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
