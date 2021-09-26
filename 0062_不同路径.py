from scipy.special import comb


# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# 组合数
# 从左上角到右下角的过程中，我们需要移动 m+n-2 次，其中有 m-1 次向下移动，
# n-1n−1 次向右移动。因此路径的总数，就等于从 m+n-2 次移动中选择 m-1 次向下移动的方案数
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)


if __name__ == '__main__':
    print(Solution().uniquePaths(m=3, n=7))
