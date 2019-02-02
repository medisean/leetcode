import UIKit

class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var i = 0
        var j = 0
        var sortedNumbers: [Int] = []
        while i < nums1.count || j < nums2.count {
            if i == nums1.count {
                sortedNumbers.append(nums2[j])
                j += 1
            } else if j == nums2.count {
                sortedNumbers.append(nums1[i])
                i += 1
            } else if nums1[i] < nums2[j] {
                sortedNumbers.append(nums1[i])
                i += 1
            } else {
                sortedNumbers.append(nums2[j])
                j += 1
            }
        }
        if sortedNumbers.count % 2 == 0 {
            return (Double(sortedNumbers[sortedNumbers.count / 2 - 1]) + Double(sortedNumbers[sortedNumbers.count / 2])) / 2
        } else {
            return Double(sortedNumbers[sortedNumbers.count / 2])
        }
    }
}

let num1 = [1, 3]
let num2 = [2]
let solution = Solution()
print(solution.findMedianSortedArrays(num1, num2))

let num3 = [1, 2]
let num4 = [3, 4]
print(solution.findMedianSortedArrays(num3, num4))
