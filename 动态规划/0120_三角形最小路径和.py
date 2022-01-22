from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        integer_max = float('inf')
        # 设f[i][j]为：从点(0, 0)出发到(i, j)的最小路径和
        n = len(triangle)
        f = [[integer_max] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                f[i][j] = triangle[i][j]
                if i > 0:
                    if j < i:
                        f[i][j] += min(f[i-1][j-1], f[i-1][j])
                    else:
                        f[i][j] += f[i-1][j-1]

        return int(min([f[n-1][x] for x in range(n)]))
