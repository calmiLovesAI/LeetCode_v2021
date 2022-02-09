from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        for i in range(m):
            if matrix[i][-1] == target:
                return True
            if matrix[i][-1] > target:
                row = i
                break

        # 矩阵第row行二分查找target
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False