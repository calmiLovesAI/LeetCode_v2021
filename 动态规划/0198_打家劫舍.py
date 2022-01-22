from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 设f[i]：最后一个被偷的房屋位置是i的情况下的最高金额
        n = len(nums)
        f = [0] * n
        ans = 0
        for i in range(n):
            f[i] = nums[i]
            t = 0
            for j in range(i-1):
                t = max(t, f[j])
            f[i] += t
            ans = max(ans, f[i])
        return ans
