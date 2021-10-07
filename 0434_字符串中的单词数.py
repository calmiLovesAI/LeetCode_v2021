


class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        pre = ""
        cnt = 0
        for i in range(n):
            if i == n - 1 and s[i] != " ":
                cnt += 1
            if i >= 1 and s[i] == " " and pre != " ":
                cnt += 1
            pre = s[i]
        if pre == "":
            return 0
        return cnt


if __name__ == '__main__':
    print(Solution().countSegments("Hello, my name is John"))