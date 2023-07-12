class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(start):
            if start == (len(nums) - 1):
                return 0

            result = -1

            for i in range(start + 1, len(nums)):
                if -target <= (nums[i] - nums[start]) <= target:
                    temp = dfs(i) + 1
                    if temp > result:
                        result = temp
            if result <= 0:
                return -1
            return result

        return dfs(0)

