from typing import List
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        result=0
        n=len(nums)
        if nums[0]==1 and nums[-1]==n:
            return result

        one_pos=nums.index(1)
        n_pos=nums.index(n)

        if one_pos>n_pos:
            result-=1

        result+=one_pos+(n-n_pos-1)

        return result


if __name__ == '__main__':
    obj=Solution()
    print(obj.semiOrderedPermutation([2,1,4,3]))
    print(obj.semiOrderedPermutation([2,4,1,3]))
    print(obj.semiOrderedPermutation([1,3,4,2,5]))


