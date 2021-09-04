


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = int((dp[i-1] + dp[i-2]) % (1e9+7))    # 在递推过程中进行取余运算
        return dp[-1]



if __name__ == '__main__':
    print(Solution().fib(81))