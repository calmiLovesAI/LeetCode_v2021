from typing import List


class Solution:
    def __init__(self):
        self.visited = None
        self.m = 0  # 长
        self.n = 0  # 宽
        self.res = 0  # 最大面积
        self.current_area = 0  # 当前岛屿的面积

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return

        if grid[i][j] == 0:
            return
        if self.visited[i][j]:
            return

        self.current_area += 1
        self.visited[i][j] = True
        # 上下左右四个方向搜索
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

        return self.current_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    self.res = max(self.res, self.dfs(grid, i, j))
                    self.current_area = 0
        return self.res


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
