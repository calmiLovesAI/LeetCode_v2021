import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) // 2
            if self.get_value(mid, nums) > self.get_value(mid-1, nums) and self.get_value(mid, nums) > self.get_value(mid+1, nums):
                ans = mid
                break
            if self.get_value(mid, nums) < self.get_value(mid-1, nums):
                j = mid - 1
            else:
                i = mid + 1
        return ans


    def get_value(self, index, arr):
        if index == -1 or index == len(arr):
            return -math.inf
        else:
            return arr[index]


if __name__ == '__main__':
    print(Solution().findPeakElement([3, 1, 2]))