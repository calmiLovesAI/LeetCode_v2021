from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]

        for char in s:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return list(map("".join, ans))


if __name__ == '__main__':
    print(Solution().letterCasePermutation(s="a1b2"))
