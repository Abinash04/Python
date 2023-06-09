'''
1.
https://leetcode.com/problems/two-sum/description/
'''

'''
nums = [11,15,7,2]

as we know that index is paired with the list values so we can consider using dictionary/hashmap.
also to get the index from the list we can use enumerate by using for loop.

create empty dictionary
dict1 = {}

for idx, value in enumerate(nums):
	# add the idx and value in the dict
	# target - 1st element of the list and then search for the result in the entire list.
	result = target - value 	# 9 - 2 = 7; 
	# 1st iteration:idx:0,val:11; 9 - 11 = -2
	# 2nd iteration: idx:1,val:15; 9 - 15 = -6
	# 3rd iter: idx:2, val: 7; 9 - 7 = 2
	# 4rth iter: idx:3, val:2; 9 - 2 = 7
	
	# search for 7 in dictionary and not in the list as it will cause to search the entire list.
	if result in dict1: 	
		# -2 is not in dict which is currently empty.
		# if found result then stop the execution as we would have found the 2nd number which will form the 
		# target
		# 1st iter: -2 not in dict {}
		# 2nd iter: -6 not in dict {11:0}
		# 3rd iter: 2 not in dict {11:0, 15:1}
		# 4th iter: 7 present in dict { 11: 0 , 15:1, 7:2}
		return [dict1[result],  idx]	# as desired output is list so frame the answer accordingly.
		# [dict1[7] = 2 and idx=3] so final_output is [2,3]
	
	dict1[value] = idx	# add the value to dictionary : {2 : 0}, 2 is the val and 0 is the index.
	# 1st iteration { 11: 0 }
	# 2nd iteration { 11: 0 , 15:1}
	# 3rd iter: { 11: 0 , 15:1, 7:2}
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # print(nums)
        # print(target)

        # get the difference between target and the individual number
        dict1 = {}
        for idx, value in enumerate(nums):
            number_to_search = target - value # 9 - 2 = 7
            if number_to_search in dict1:
                return [dict1[number_to_search], idx]
            dict1[value] = idx

            



sol = Solution()
print(sol.twoSum([2,7,11,15], 9))