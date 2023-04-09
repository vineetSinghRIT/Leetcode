from typing import List
import math
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:

        prefix=1
        end=math.prod(nums)

        for i in range(len(nums)-1):
            prefix*=nums[i]
            suffix=end//prefix

            if math.gcd(prefix,suffix)==1:
                return i

        return -1


if __name__ == '__main__':
    obj=Solution()
    print(obj.findValidSplit([4,7,8,15,3,5]))
    print(obj.findValidSplit([4,7,15,8,3,5]))

