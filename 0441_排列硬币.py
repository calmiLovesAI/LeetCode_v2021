


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        pre = 1
        for i in range(1, n):
            cur = pre + (i+1)
            if cur == n:
                return i + 1
            if cur > n > pre:
                return i
            pre = cur

# 解法二：二分查找
class Solution2:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) / 2 <= n:
                left = mid
            else:
                right = mid - 1
        return left



if __name__ == '__main__':
    print(Solution2().arrangeCoins(1804289383))