'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        d = {1: 1}
        for i in range(2, n+1):
            d[i] = d[i-1] * i

        s = ''
        nums = [j for j in range(1, n+1)]
        for i in range(n):
            if i == n-1:
                s += str(nums[0])
                break
            r = 0
            for j in range(n-i):
                if r + d[n-i-1] < k:
                    r += d[n-i-1]
                else:
                    s += str(nums[j])
                    nums.pop(j)
                    k -= r
                    break
        return s

if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(1, 1))