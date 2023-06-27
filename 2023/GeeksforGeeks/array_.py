from typing import List

'''
For Input: 
4
-3 3 -2 2
'''

class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        # code here
        count = 0
        str1 = ""
        str2 = ""
        for val in arr:
            if val < 0:
                str1 += str(val) + " " # -3 -2
                # arr.remove(val) # arr = [3, -2, 2]
                print(str1, arr)
            else:
                str2 += str(val) + " " # 3 2
                # arr.remove(val) # [-2, 2]
                print(str1, arr)
    
        arr.insert(0, str1)
        arr.insert(1, str2)
        print(str1 + str2)
            

sol = Solution()
print(sol.Rearrange(4, [-3 ,3 ,-2, 2]))