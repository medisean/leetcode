import UIKit

/*
 
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 
 P   A   H   N
 A P L S I I G
 Y   I   R
 And then read line by line: "PAHNAPLSIIGYIR"
 
 Write the code that will take a string and make this conversion given a number of rows:
 
 string convert(string s, int numRows);
 Example 1:
 
 Input: s = "PAYPALISHIRING", numRows = 3
 Output: "PAHNAPLSIIGYIR"
 Example 2:
 
 Input: s = "PAYPALISHIRING", numRows = 4
 Output: "PINALSIGYAHRPI"
 Explanation:
 
 P     I    N
 A   L S  I G
 Y A   H R
 P     I
 
思路：
    第一行 n 个
    第二到 n - 1 行 1 个
 
    n = 3
    第一行 3 个
    第二行 1 个
    第三行 3 个
    第四行 1 个
 
    s = 14 个字符，那么有 14 / 4 = 3
 
    n = 4
    第一行 4 个
    第二行 1 个
    第三行 1 个
 
    n 行
    共有 n - 1 种行情况
 
    设置一个二维数组，先将字符串转化为二维数组，再读取
 
    第 0 个元素，对应第 0 列 第 0 行
    第 1 个元素，对应第 0 列 第 1 行
    第 i 个元素，对应第 xxx 列 第 xxx 行
    第 4 个元素，从头到尾读取
 
    f(x) = ax + by
 
    思路二：
    找出每行的元素，然后输出，即找出元素和行的对应关系
    假设为 3 行， 2列，共 3 + 1 = 4 个元素
        第一行，第 0 个元素，第 4 个元素，第 8 个元素   n / 4 == 0
        第二行，第 1 个元素，第 3 个元素，第 5 个元素   (n + 1) / 4
        第三行，第 2 个元素，第 6 个元素              n + 4
    假设为 4 行，共 3 列，共 4 + 2 = 6 个元素
        第一行，第 0 个元素，第 6 个元素，第 12 个元素   n / 6
        第二行，第 1 个元素，第 5 个元素，第 7 个元素，第 11 个元素    (n - 1) / 6 || (n - 1) / 4
        第三行，第 2 个元素，第 4 个元素，第 8 个元素，第 10 个元素 (n - 2) / 6 || (n - 2) /
        第四行，第 3 个元素，第 9 个元素
 */

class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 {
            return s
        }
        var strings: [String] = []
        for _ in 0..<numRows {
            strings.append("")
        }
        
        var isAdd = true
        var addedIndex = 0
        for (_, value) in s.enumerated() {
            strings[addedIndex].append(value)

            if isAdd {
                if addedIndex + 1 >= numRows {
                    isAdd = false
                    addedIndex -= 1
                } else {
                    addedIndex += 1
                }
            } else {
                if addedIndex - 1 < 0 {
                    isAdd = true
                    addedIndex = 1
                } else {
                    addedIndex -= 1
                }
            }
        }
        var result = ""
        for string in strings {
            result += string
            strings.append("")
        }
        return result
    }
}

let s = "AB"
let solution = Solution()
print(solution.convert(s, 1))
