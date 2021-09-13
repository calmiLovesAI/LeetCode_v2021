from typing import List
from collections import defaultdict

import math


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            cnt = defaultdict(int)
            for q in points:
                dis = math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2)
                cnt[dis] += 1
            for m in cnt.values():
                ans += m * (m - 1)
        return ans
