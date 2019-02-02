import UIKit

/**
 Given a string, find the length of the longest substring without repeating characters.
 
 Example 1:
 
 Input: "abcabcbb"
 Output: 3
 Explanation: The answer is "abc", with the length of 3.
 Example 2:
 
 Input: "bbbbb"
 Output: 1
 Explanation: The answer is "b", with the length of 1.
 Example 3:
 
 Input: "pwwkew"
 Output: 3
 Explanation: The answer is "wke", with the length of 3.
 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

 **/
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var longestSubStringCount = 0
        var character: [Character] = []
        var map: [Character: Int] = [:]

        for c in s {
            if map[c] != nil {
                
            } else {
                map
            }
            if let index = character.firstIndex(of: c) {
                let range = 0..<(index+1)
                character.removeSubrange(range)
            }
            character.append(c)
            longestSubStringCount = max(character.count, longestSubStringCount)
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
