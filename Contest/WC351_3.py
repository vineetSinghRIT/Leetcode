from operator import mod
from typing import  List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        pos = []

        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)

        if len(pos) == 0 or len(pos) == 1:
            return len(pos)

        result = 1
        for i in range(1, len(pos)):
            zeros = pos[i] - pos[i - 1] - 1
            if zeros != 0:
                result = mod(result * (zeros + 1), 1000000007)

        return result % (1000000007)
