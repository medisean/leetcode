import UIKit

//
//  #7 Reverse Integer.swift
//
//
//  Created by bruce on 2019/2/17.
//

import Foundation

/*
 
 Given a 32-bit signed integer, reverse digits of an integer.
 
 Example 1:
 
 Input: 123
 Output: 321
 Example 2:
 
 Input: -123
 Output: -321
 Example 3:
 
 Input: 120
 Output: 21
 */
class Solution {
    func reverse(_ x: Int) -> Int {
        let maxNumber = 2 << 30
        let min = -Int(maxNumber)
        let max = Int(maxNumber - 1)
        var result = 0
       
        var s = String(x)
        if s.first == "-" {
            s.removeFirst()
            s = String(s.reversed())
            result = -Int(s)!
        } else {
            s = String(s.reversed())
            result = Int(s)!
        }
        
        if result > max || result < min {
            return 0
        }
        return result
    }
}

let solution = Solution()
print(solution.reverse(1563847412))

