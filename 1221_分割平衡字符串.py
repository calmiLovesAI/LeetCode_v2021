

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 变量d维护L和R字符的数量之差，当 d=0时就说明找到了一个平衡字符串
        ans, d = 0, 0
        for ch in s:
            if ch == 'L':
                d += 1
            else:
                d -= 1
            if d == 0:
                ans += 1
        return ans



if __name__ == '__main__':
    print(Solution().balancedStringSplit(s="RLRRRLLRLL"))


