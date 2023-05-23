"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        bsearch=self.helper(nums,0,len(nums)-1)
        return nums[bsearch]

    def helper(self,nums,left,right):

        mid=left+((right-left)//2)

        if left==right or (nums[mid-1]>nums[mid]):
            return mid

        else:
            if nums[mid]>nums[left] and nums[mid]>nums[right]:
                return self.helper(nums,mid+1,right)
            else:
                return self.helper(nums, left, mid-1)

if __name__ == '__main__':
    obj=Solution()
    print(obj.findMin([3,4,5,1,2]))
    print(obj.findMin([4,5,6,7,0,1,2]))
    print(obj.findMin([11,13,15,17]))
    print(obj.findMin([2,1]))
    print(obj.findMin([0,1]))