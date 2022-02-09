from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找第一个小于nums[0]的元素位置
        t = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= t:
                l = mid + 1
            else:
                r = mid
        return min(t, nums[l])


if __name__ == '__main__':
    print(Solution().findMin([11, 13, 15, 17]))
