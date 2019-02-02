import UIKit

/**
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
 
 Example:
 
 Given nums = [2, 7, 11, 15], target = 9,
 
 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].
 **/

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
