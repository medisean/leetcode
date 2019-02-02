import UIKit

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var longestSubStringCount = 0
        var chracters: [Character] = []

        for c in s {
            if let index = chracters.firstIndex(of: c) {
                let range: Range<Int> = 0..<(index+1)
                chracters.removeSubrange(range)
            }
            chracters.append(c)
            longestSubStringCount = max(chracters.count, longestSubStringCount)
        }
        return longestSubStringCount
    }
}

let str = "aabaab!bb"
let solution = Solution()
print(solution.lengthOfLongestSubstring(str))


let str2 = "pwwkew"
print(solution.lengthOfLongestSubstring(str2))

let str3 = "dvdf"
print(solution.lengthOfLongestSubstring(str3))

let str4 = "bbbb"
print(solution.lengthOfLongestSubstring(str4))
