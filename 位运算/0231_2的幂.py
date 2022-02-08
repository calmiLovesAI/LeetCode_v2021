class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n / 2
        if n == 1:
            return True
        else:
            return False


"""
一个数n是2的幂，当且仅当n是正整数，并且n的二进制表示中仅包含1个 1。

因此我们可以考虑使用位运算，将n的二进制表示中最低位的那个1提取出来，再判断剩余的数值是否为0即可。
如果n是正整数并且n&(n-1) = 0，那么n就是2的幂。
"""


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(16))
