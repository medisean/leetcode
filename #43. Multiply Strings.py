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
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]

        results = []
        for i in range(len(num1)):
            result = ''
            numI = int(num1[i])
            addition = 0
            for j in range(len(num2)):
                temp = int(num2[j]) * numI + addition
                result = str(temp%10) + result
                addition = int(temp / 10)
            if addition != 0:
                result = str(addition) + result
            result += i * '0'
            results.append(result)
        s = ''
        for result in results:
            s = self.add(s, result)
        return s
    def add(self, str1: str, str2: str) -> str:
        result = ''
        str1 = str1[::-1]
        str2 = str2[::-1]
        addition = 0
        maxLength = max(len(str1), len(str2))
        i = 0
        while i < maxLength:
            if i < len(str1) and i < len(str2):
                t = int(str1[i]) + int(str2[i]) + addition
            elif i < len(str1):
                t = int(str1[i]) + addition
            else:
                t = int(str2[i]) + addition
            if t >= 10:
                addition = 1
                t = t % 10
            else:
                addition = 0
            result = str(t) + result
            i += 1
        if addition != 0:
            result = '1' + result
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply('123', '456'))
    print(solution.add('123', '956'))
