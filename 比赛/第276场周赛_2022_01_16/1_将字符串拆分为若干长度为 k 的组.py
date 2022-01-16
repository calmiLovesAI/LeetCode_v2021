from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        st = ""
        for i in range(len(s)):
            st += s[i]
            if i == len(s) - 1 and len(st) < k:
                st += fill * (k - len(st))
                res.append(st)
            if (i+1) % k == 0:
                res.append(st)
                st = ""
        return res


if __name__ == '__main__':
    print(Solution().divideString(s="abcdefghij", k=3, fill="x"))
