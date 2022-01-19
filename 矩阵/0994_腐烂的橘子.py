from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # 找出所有的"2"，然后放入队列
        m = len(grid)
        n = len(grid[0])
        q = deque()
        flag = True
        t = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag = False
                if grid[i][j] == 2:
                    q.append([i, j])

        if flag:
            return 0

        while q:
            size = len(q)
            for k in range(size):
                i, j = q.popleft()
                directions = ([i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1])
                for d in directions:
                    if 0 <= d[0] < m and 0 <= d[1] < n and grid[d[0]][d[1]] == 1:
                        grid[d[0]][d[1]] = 2
                        q.append(d)
            t += 1

        # 判断是否还剩余1
        flag = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag = False

        if not flag:
            return -1
        return t


if __name__ == '__main__':
    print(Solution().orangesRotting(grid=[[0, 2]]))
