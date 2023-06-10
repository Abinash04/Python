'''
1920.
https://leetcode.com/problems/build-array-from-permutation/
'''

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans

sol = Solution()
print(sol.buildArray([0,2,1,5,3,4]))