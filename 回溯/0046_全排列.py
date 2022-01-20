from collections import deque
from copy import deepcopy
from typing import List


# 深度优先遍历
class Solution:
    def __init__(self):
        self.used = None
        self.temp = []
        self.res = []

    def dfs(self, nums, k):
        if k == len(nums):
            self.res.append(deepcopy(self.temp))
            return
        for i in range(len(self.used)):
            if not self.used[i]:
                self.temp.append(nums[i])
                self.used[i] = True
                self.dfs(nums, k + 1)
                # 状态重置
                self.temp.pop(-1)
                self.used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.used = [False] * n
        self.dfs(nums, 0)
        return self.res


# 广度优先遍历
class SolutionBFS:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        temp = []
        q = deque([[_] for _ in range(n)])    # index

        while q:
            idx_list = q.popleft()
            if len(idx_list) == n:
                res.append([nums[i] for i in idx_list])
                continue
            for idx in idx_list:
                used[idx] = True
            temp.extend(idx_list)
            for i in range(n):
                if not used[i]:
                    temp.append(i)
                    q.append(temp.copy())
                    temp.pop(-1)
            # reset
            temp = []
            used = [False] * n
        return res


if __name__ == '__main__':
    print(SolutionBFS().permute([1, 2, 3]))
