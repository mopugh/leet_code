# My solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substrings = []
#         if s == '':
#             return 0
#         for i,s in enumerate(s):
#             if i == 0:
#                 substrings.append(s[0])
#             else:
#                 if s in substrings[-1]:
#                     # find previous occurrence
#                     ind = substrings[-1].find(s)
#                     substrings.append(substrings[-1][ind+1:] + s)
#                 else:
#                     substrings.append(substrings[-1] + s)
#         # Find longest
#         # print(substrings)
#         return len(max(substrings,key=len))

# Optimized Solution
# Use a hashmap to keep track of indices and locations
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans