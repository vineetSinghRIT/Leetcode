"""
https://leetcode.com/problems/sort-colors/
"""
from typing import List
class SortColors:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        l, r = 0, len(nums) - 1

        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

        while curr <= r:
            if nums[curr] == 0:
                swap(l, curr)
                l += 1

            elif nums[curr] == 2:
                swap(curr, r)
                r -= 1
                curr -= 1
            curr += 1

    def sortColorsFT(self, nums: list[int]) -> None:
        color=[0]*3

        for val in nums:
            color[val]+=1

        for i in range(1,3):
            color[i] = color[i] + color[i - 1]

        checked=[0]*len(nums)


        end=len(nums)-1
        for i in range((len(nums)*2)-1,-1,-1):
            valE=nums[end]
            toEX=color[valE]-1

            if checked[toEX]==1 or toEX==end or checked[end]==1:
                checked[end]=1
                end-=1
                continue

            color[valE]-=1

            #Exchange
            temp=nums[end]
            nums[end]=nums[toEX]
            nums[toEX]=temp

            checked[toEX]+=1


        return  nums

if __name__ == '__main__':
    obj=SortColors()
    print(obj.sortColors([0,2,1]))



