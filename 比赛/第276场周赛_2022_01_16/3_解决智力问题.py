from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * n
        res = 0
        for i in range(n-1, -1, -1):
            if i == n - 1:
                f[i] = questions[i][0]
            else:
                if i+1+questions[i][1] < n:
                    f[i] = max(f[i+1], questions[i][0] + f[i+1+questions[i][1]])
                else:
                    f[i] = max(f[i+1], questions[i][0])
            res = max(res, f[i])
        return res


if __name__ == '__main__':
    print(Solution().mostPoints([[12,46],[78,19],[63,15],[79,62],[13,10]]))
