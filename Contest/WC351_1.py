class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if self.gcd(int(str(nums[i])[0]), int(nums[j] % 10)) == 1:
                    result += 1

        return result

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)