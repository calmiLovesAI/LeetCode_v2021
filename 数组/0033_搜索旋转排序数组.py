from typing import List


class Solution:
    def binary_search(self, arr, i, j, target):
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        t = 0
        for i in range(right):
            if nums[i] > nums[i + 1]:
                t = i
                break
        # 分段二分查找
        res_1 = self.binary_search(nums, left, t, target)
        res_2 = self.binary_search(nums, t+1, right, target)
        if res_1 != -1:
            return res_1
        if res_2 != -1:
            return res_2
        return -1


# 一遍二分查找
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution2().search([3, 1], 1))