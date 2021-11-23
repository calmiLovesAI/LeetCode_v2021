class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        inds = []
        for i in range(n):
            if s[i] != goal[i]:
                inds.append(i)
        # 两个字符串相等并且至少有2个位置的字符相等
        if s == goal:
            char_set = set()
            for c in s:
                if c in char_set:
                    return True
                else:
                    char_set.add(c)
        if len(inds) != 2:
            return False
        if s[inds[0]] == goal[inds[1]] and s[inds[1]] == goal[inds[0]]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().buddyStrings(s="aa", goal="aa"))
