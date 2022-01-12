from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        while left < right:
            s = numbers[left-1] + numbers[right-1]
            if s == target:
                return [left, right]
            elif s > target:
                right -= 1
            else:
                left += 1