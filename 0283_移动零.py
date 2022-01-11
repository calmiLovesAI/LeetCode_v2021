from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                j = i
                while j < n and nums[j] == 0:
                    j += 1
                if j < n:
                    # 交换
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
            i += 1


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        # 左指针左边均为非零数；
        # 右指针左边直到左指针处均为零
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
