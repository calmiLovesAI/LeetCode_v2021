from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        # 这三个数的索引分别为a, b, c， 且有a < b < c
        nums.sort()
        ans = []
        a = 0
        while a < n:
            b = a + 1
            c = n - 1
            while b < c:
                if nums[a] + nums[b] + nums[c] == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    # 找到下一个不等于nums[b]的位置
                    k = nums[b]
                    while b < n and nums[b] == k:
                        b += 1
                elif nums[a] + nums[b] + nums[c] < 0:
                    b += 1
                else:
                    c -= 1
            # 找到下一个不等于nums[a]的位置
            t = nums[a]
            while a < n and nums[a] == t:
                a += 1
            if a == n:
                break
        return ans


if __name__ == '__main__':
    print(Solution().threeSum(nums=[0, 0, 0, 0]))
