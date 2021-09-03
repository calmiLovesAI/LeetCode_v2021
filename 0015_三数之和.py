from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()   # 从小到大排序
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            k = n - 1
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while nums[i] + nums[j] + nums[k] > 0 and k > j:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([3, -2, 1, 0]))