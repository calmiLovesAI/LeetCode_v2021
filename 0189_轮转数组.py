from typing import List


class Solution:
    def reverse(self, arr: List[int], start: int, end: int):
        while start < end:
            # 交换
            t = arr[start]
            arr[start] = arr[end]
            arr[end] = t
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 先翻转整个数组
        self.reverse(nums, 0, n - 1)
        # 翻转[0, k-1]区间
        self.reverse(nums, 0, k - 1)
        # 翻转[k, n-1]区间
        self.reverse(nums, k, n - 1)
