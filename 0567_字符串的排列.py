import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        cnt = [0] * 26
        if m > n:
            return False
        for i in range(m):
            cnt[ord(s2[i]) - ord("a")] += 1
            cnt[ord(s1[i]) - ord("a")] -= 1
        diff = sum(list(map(lambda x: 0 if x == 0 else 1, cnt)))
        if diff == 0:
            return True
        for j in range(m, n):
            x = ord(s2[j]) - ord("a")
            y = ord(s2[j-m]) - ord("a")
            if x == y:
                continue
            if cnt[x] == 0:
                diff += 1
            cnt[x] += 1
            if cnt[x] == 0:
                diff -= 1
            if cnt[y] == 0:
                diff += 1
            cnt[y] -= 1
            if cnt[y] == 0:
                diff -= 1
            if diff == 0:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("abc", "bbbca"))