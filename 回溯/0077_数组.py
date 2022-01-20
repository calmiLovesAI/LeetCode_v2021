from typing import List


class Solution:
    def __init__(self):
        self.temp = []
        self.ans = []

    def dfs(self, cur, n, k):
        if len(self.temp) + (n - cur + 1) < k:
            return
        if len(self.temp) == k:
            self.ans.append(self.temp.copy())
            return
        self.temp.append(cur)
        self.dfs(cur+1, n, k)
        self.temp.pop(-1)
        self.dfs(cur + 1, n, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.dfs(1, n, k)
        return self.ans
