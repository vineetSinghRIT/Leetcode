from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        while left<=right:

            mid=left+((right-left)//2)
            if nums[mid]==target:
                return mid
            if left==right:
                return -1

            if mid==left and target==nums[right]:
                return right

            else:
                if nums[mid]>nums[left]:
                    if target>nums[mid]:
                        left=mid+1
                    else:
                        if target<nums[mid]:
                            if target>=nums[left]:
                                right=mid-1
                            else:
                                left=mid+1
                else:
                    if target>nums[mid]:
                        if target>nums[right]:
                            right=mid-1
                        else:
                            left=mid+1
                    else:
                        right=mid-1
        return -1

if __name__ == '__main__':
    obj=Solution()
    print(obj.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(obj.search(nums = [4,5,6,7,0,1,2], target = 3))
    print(obj.search(nums = [4,5,6,7,0,1,2], target = 6))
    print(obj.search(nums = [1], target = 0))
    print(obj.search(nums = [1,3], target = 3))
    print(obj.search(nums = [5,1,3], target = 3))