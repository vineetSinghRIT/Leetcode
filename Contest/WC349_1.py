from typing import List
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        if len(nums)<=2:
            return -1
        temp=nums[0:3]
        temp.sort()

        return temp[1]

if __name__ == '__main__':
    obj=Solution()
    print(obj.findNonMinOrMax([3,2,1,4]))
    print(obj.findNonMinOrMax([1,2]))
    print(obj.findNonMinOrMax([2,1,3]))