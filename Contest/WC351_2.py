
"""
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
"""

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            num1 -= num2
            if num1 >= i and num1.bit_count() <= i:
                return i

        return -1
