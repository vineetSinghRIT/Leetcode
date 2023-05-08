from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefixSet=set()
        suffixSet=set()
        LL = len(nums)
        prefix = [1]*LL
        suffix = [0]*LL

        prefixSet.add(nums[0])


        for i in range(1,LL):

            if nums[i] not in prefixSet:
                prefixSet.add(nums[i])

            prefix[i] = len(prefixSet)

            if nums[LL-i] not in suffixSet:
                suffixSet.add(nums[LL-i])
            suffix[LL - i - 1] = len(suffixSet)

        result=[prefix[i]-suffix[i] for i in range(LL)]


        return result






if __name__ == '__main__':
    obj=Solution()
    print(obj.distinctDifferenceArray([1,2,3,4,5]))
    print(obj.distinctDifferenceArray([3,2,3,4,2]))
    print(obj.distinctDifferenceArray([4,4,4,4,4]))

