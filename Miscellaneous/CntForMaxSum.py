"""
https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/
"""

from typing import List
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        resultM = 0
        cnt = 0
        lkup = set(banned)
        for i in range(1, n + 1):
            if i not in lkup and (resultM + i) <= maxSum:
                resultM += i
                cnt += 1
            elif resultM + i > maxSum:
                break

        return cnt

