class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        result_index_list = []
        while left < right:
            if nums[left] + nums[right] > target:
                right -=1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                result_index_list.append(left,right)
            left +=1
        return result_index_list

sol = Solution()
print(sol.twoSum([2,7,11,15]), 9)
