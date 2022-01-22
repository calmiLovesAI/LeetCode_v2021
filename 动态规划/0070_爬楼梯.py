class Solution:
    def climbStairs(self, n: int) -> int:
        # f[i] 表示到第i级阶梯的方法
        # f[i] = f[i-1] + f[i-2]
        f = [1] * (n+1)
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]