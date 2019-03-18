'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        results = []
        for i in range(len(num1)):
            result = ''
            numI = int(num1[i])
            addition = 0
            for j in range(len(num2)):
                temp = int(num2[j]) * numI + addition
                result = str(temp%10) + result
                addition = int(temp / 10)
            results.append(result)
        print(results)
        return ''

if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply('123', '456'))
