import pdb
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        nums_with_index = sorted(enumerate(nums), key= lambda x:x[1]) # a tuple with 1st element as index and second as original value
        while left < right:
            sum = nums_with_index[left][1] + nums_with_index[right][1]
            if sum > target:
                right -=1
            elif sum < target:
                left += 1
            else:
                return [nums_with_index[left][0], nums_with_index[right][0]]
            


sol = Solution()
print(sol.twoSum([1,2,3], 3))