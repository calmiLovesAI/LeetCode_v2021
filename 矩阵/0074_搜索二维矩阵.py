from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # 对矩阵的最后一列进行二分查找，找出第1个大于target的数的序号
        l, r = 0, m - 1
        while l < r:
            middle = (l + r) // 2
            if matrix[middle][-1] > target:
                r = middle
            else:
                l = middle + 1
        # 考虑一种特殊情况
        if l > 0 and matrix[l-1][-1] == target:
            row = l - 1
        else:
            row = l

        # 矩阵第row行二分查找target
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
