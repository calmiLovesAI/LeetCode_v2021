from typing import List

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]




if __name__ == '__main__':
    ans = Solution().smallestK(arr=[1, 3, 2, 4, 5, 6], k=3)
    print(ans)