from typing import List

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [0]

        leftA=[0]*len(nums)
        rightA=[0]*len(nums)
        left=0
        right=0

        for i in range(0,len(nums)):
            left+=nums[i]
            right+=nums[len(nums)-1-i]
            leftA[i]=left
            rightA[len(nums)-1-i]=right

        result=[abs(leftA[i]-rightA[i]) for i in range(len(nums))]

        return result

if __name__ == '__main__':
    obj=Solution()
    print(obj.leftRigthDifference([10,4,8,3]))
    print(obj.leftRigthDifference([1]))

