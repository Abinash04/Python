'''14.
https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        word_to_compare = min(strs, key=len)

        for i in strs:
            if word_to_compare[0] != i[0]:
                return ""
            else:


sol = Solution()
strs = ["flower","flow","flight"]
sol.longestCommonPrefix(strs)