import UIKit


class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var map: [Int: Int] = [:]
        for i in 0..<nums.count {
            if map.keys.firstIndex(of: target-nums[i]) != nil {
                return [map[target-nums[i]]!, i]
            }
            map[nums[i]] = i
        }
        
//        for i in 0..<nums.count {
//            for j in i+1..<nums.count {
//                if nums[j] == target - nums[i] {
//                    return [i, j]
//                }
//            }
//        }
        return []
    }
}

let nums = [3,2,3]
let solution = Solution()
solution.twoSum(nums, 6)
