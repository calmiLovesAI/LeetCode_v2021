from typing import List


class Solution:
    def binary_search_first(self, arr, target):
        start = 0
        end = len(arr) - 1
        while start <= end:
            middle = (start + end) // 2
            if arr[middle] == target:
                if start == end:
                    return middle
                end = middle
            elif arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        first_idx = self.binary_search_first(nums, target)
        if first_idx == -1:
            return [-1, -1]
        last_idx = self.binary_search_last(nums, target)
        return [first_idx, last_idx]

    def binary_search_last(self, arr, target):
        start = 0
        end = len(arr) - 1
        while start <= end:
            middle = (start + end + 1) // 2    # 上取整
            if arr[middle] == target:
                if start == end:
                    return middle
                start = middle
            elif arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return -1


if __name__ == '__main__':
    print(Solution().searchRange([0, 0, 1, 1, 1, 1, 1], 1))
