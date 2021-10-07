from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        idx = 0
        for i in range(len(nums)):
            if i == 0:
                idx += 1
            if i > 0 and nums[i] != nums[i-1]:
                idx += 1
            if idx == 3:
                return nums[i]
        return nums[0]
