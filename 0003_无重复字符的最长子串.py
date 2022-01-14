
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针、滑动窗口
        n = len(s)
        left, right = 0, 0
        c = set()  # left和right之间的字符集合
        res = 0
        while right < n:
            if s[right] not in c:
                c.add(s[right])
                if right == n - 1:
                    return max(res, len(c))
                right += 1
            else:
                res = max(res, len(c))
                c.remove(s[left])
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s="xxabc"))