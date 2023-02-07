from typing import List


class allGood:
    def non_increasing(self,L):
        return all(x >= y for x, y in zip(L, L[1:]))

    def non_decreasing(self,L):
        return all(x <= y for x, y in zip(L, L[1:]))
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        res=[]
        found=False
        for i in range(k,len(nums)):

            if found==False and self.non_increasing(nums[i-k:i]) and i+1+k<=len(nums) and self.non_decreasing((nums[i+1:i+1+k])):
                res.append(i)

            elif found==True:
                if nums[i-1]<=nums[i-2] and nums[i+k]>=nums[i+k-1]:
                    res.append(i)
                else:
                    found==False


        return res

if __name__ == '__main__':
    obj=allGood()
    print(obj.goodIndices(nums = [2,1,1,1,3,4,1], k = 2))
    print(obj.goodIndices(nums = [2,1,1,2], k = 2))
    print(obj.goodIndices(nums = [440043,276285,336957], k = 1))