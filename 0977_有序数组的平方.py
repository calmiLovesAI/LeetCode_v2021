from typing import List


class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        res = []
        while i < j:
            s_i = nums[i] ** 2
            s_j = nums[j] ** 2
            if s_i > s_j:
                i += 1
                res.append(s_i)
            elif s_i < s_j:
                j -= 1
                res.append(s_j)
            else:
                res.append(s_i)
                res.append(s_j)
                i += 1
                j -= 1
        if i == j:
            res.append(nums[i] ** 2)
        return res[::-1]


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 找到第一个大于0的数
        n = len(nums)
        t0 = -1
        for i in range(n):
            if nums[i] >= 0:
                if i - 1 >= 0:
                    t0 = i if abs(nums[i]) < abs(nums[i-1]) else i-1
                else:
                    t0 = i
                break
        # t1向左走，t2向右走
        if t0 == -1:
            t0 = n - 1
        t1 = t0
        t2 = t0
        res = []
        while t1 >= 0 and t2 < n:
            s1 = nums[t1] ** 2
            s2 = nums[t2] ** 2
            if s1 < s2:
                res.append(s1)
                t1 -= 1
            elif s2 < s1:
                res.append(s2)
                t2 += 1
            else:
                res.extend([s1, s2]) if t1 != t2 else res.append(s1)
                t1 -= 1
                t2 += 1
        while t1 >= 0:
            res.append(nums[t1] ** 2)
            t1 -= 1
        while t2 < n:
            res.append(nums[t2] ** 2)
            t2 += 1
        return res


class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1

        return ans


if __name__ == '__main__':
    print(Solution2().sortedSquares(nums=[-1, 2, 2]))
