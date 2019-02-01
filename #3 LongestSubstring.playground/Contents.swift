import UIKit

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let nsstring = s as NSString
        
        var longestSubStringCount = 0
        var maxString: NSString = ""
        for i in 0..<nsstring.length {
            let new = nsstring.substring(with: NSRange(location: i, length: 1))
            let range = maxString.range(of: new)
            
            if range.length != 0 {
                longestSubStringCount = max(maxString.length, longestSubStringCount)
                maxString = (maxString.substring(from: range.location + 1) + new) as NSString
                continue
            }
            maxString = maxString.appending(new) as NSString
            longestSubStringCount = max(maxString.length, longestSubStringCount)
        }
        return longestSubStringCount
    }
}

let str = "abcabcbb"
let solution = Solution()
print(solution.lengthOfLongestSubstring(str))


let str2 = "pwwkew"
print(solution.lengthOfLongestSubstring(str2))

let str3 = "dvdf"
print(solution.lengthOfLongestSubstring(str3))

let str4 = "bbbb"
print(solution.lengthOfLongestSubstring(str4))
