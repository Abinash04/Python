# https://leetcode.com/problems/3sum/

''' 
15. 3sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        p1, p2, p3 = 0, 1, len(nums) - 1
        result = []
        while p1 < p3:
            if (p1 != p2 and p1 != p3) and p2 != p3:
                if nums[p1] + nums[p2] + nums[p3] == 0:
                    result.append([nums[p1], nums[p2], nums[p3]])
            # p3 -= 1
            # p1 += 1
            # p2 += 1
        return result

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
                
             