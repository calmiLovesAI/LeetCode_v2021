from typing import List


# 排序
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n


# 求和
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target_sum = int(n * (n + 1) / 2)
        arr_sum = sum(nums)
        return target_sum - arr_sum


# 位运算：异或
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= nums[i]
        for j in range(n + 1):
            xor ^= j
        return xor
