from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         set_list = set(nums)
#         for i, item in enumerate(nums):
#             new_target = target - item
#             if item != new_target and new_target in set_list:
#                 return [i, nums.index(new_target)]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         return [[j,i] for i in range(len(nums))
#                      for j in range(i)
#                      if nums[i] + nums[j] == target][0]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, item in enumerate(nums):
            new_target = target - item
            new_target_ind = d.get(new_target)
            if new_target_ind is not None:
                return [new_target_ind, i]
            else:
                d[item] = i