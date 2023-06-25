from operator import mod


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        pos = []

        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)

        if len(pos) == 0:
            return 0

        if len(pos) == 1:
            return 1

        result = 1
        for i in range(1, len(pos)):
            zeros = pos[i] - pos[i - 1] - 1
            if zeros != 0:
                result = mod(result * (zeros + 1), 1000000007)

        return result % (1000000007)
