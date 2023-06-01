import time

'''
12. https://leetcode.com/problems/roman-to-integer/

Convert string into list
str1 = "ABCDE"
list1 = ['A','B','C','D','E]

Example 1: MMCMXCIX (2999)
Example 2: MCCCLXXVII (1377)
Example 3: MMMCCXXII (3222)
Example 4: MCDXXVII (1427)
Example 5: MMMCDXLIV (3444)
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # create a dictionary
        roman_to_int_dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        # convert string into roman literal list
        roman_list = []
        roman_list[:0] = s

        # Get corresponding int value list from roman
        integer_list = []
        for i in roman_list:
            integer_list.append(roman_to_int_dict[i])

        # compare from left value to right value within the list
        # if left value is greater or equal then just append the int number
        # if left value is smaller then change the sign of the int number
        final_list = []
        for i, v in enumerate(integer_list):
            if i == len(s) - 1:
                final_list.append(v)
                break
            if integer_list[i] >= integer_list[i+1]:
                final_list.append(v)
            if integer_list[i] < integer_list[i+1]:
                final_list.append(-v)
        return sum(final_list)

start = time.time()

solution13 = Solution()
solution13.romanToInt("III")

end = time.time()
print("execution_time:", (end - start) * 1000)
