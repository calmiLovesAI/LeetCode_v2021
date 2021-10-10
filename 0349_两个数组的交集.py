from typing import List

# 排序、双指针
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        inter_list = list()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                inter_list.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(set(inter_list))