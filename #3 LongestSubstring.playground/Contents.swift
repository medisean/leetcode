import UIKit

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
