from typing import List

import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        f = [[math.inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                f[i][j] = grid[i][j]
                if i == 0 and  j == 0:
                    continue
                elif i == 0:
                    f[i][j] += f[i][j-1]
                elif j == 0:
                    f[i][j] += f[i-1][j]
                else:
                    f[i][j] += min(f[i][j-1], f[i-1][j])

        return f[m-1][n-1]


