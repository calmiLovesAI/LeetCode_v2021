# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

class Solution:
    def reverseString(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            # 交换
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)

    def reverseWords(self, s: str) -> str:
        words_list = s.split(" ")
        for i in range(len(words_list)):
            words_list[i] = self.reverseString(words_list[i])
        return " ".join(words_list)