from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.new_color = 0

    def dfs(self, matrix, i, j, c):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return
        if matrix[i][j] != c:
            return
            # 涂色
        matrix[i][j] = self.new_color
        # 上下左右
        self.dfs(matrix, i - 1, j, c)
        self.dfs(matrix, i + 1, j, c)
        self.dfs(matrix, i, j - 1, c)
        self.dfs(matrix, i, j + 1, c)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS
        self.m, self.n = len(image), len(image[0])
        self.new_color = newColor
        color = image[sr][sc]
        if color == newColor:
            return image
        self.dfs(image, sr, sc, color)
        return image


if __name__ == '__main__':
    print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
