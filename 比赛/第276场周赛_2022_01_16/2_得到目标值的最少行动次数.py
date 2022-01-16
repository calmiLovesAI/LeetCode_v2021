class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        f = [[0] * (maxDoubles + 1) for _ in range(target + 1)]
        # f[i][j]表示到达整数i处，使用了j次乘法的最少行动次数
        for i in range(2, target + 1):
            for j in range(maxDoubles + 1):
                f[i][j] = f[i - 1][j] + 1
                if i % 2 == 0 and j >= 1:
                    f[i][j] = min(f[i][j], f[i // 2][j - 1] + 1)
        return f[target][maxDoubles]


if __name__ == '__main__':
    print(Solution().minMoves(19, 2))
