class Solution1:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target > 1:
            if maxDoubles == 0:
                return cnt + target - 1
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            cnt += 1
        return cnt


# 二维动态规划
class Solution2:
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
    print(Solution1().minMoves(656101987, 1))
