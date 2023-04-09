from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        tracker=defaultdict(list)

        for i in range(len(nums)):
            tracker[nums[i]].append(i)

        result = [0] * len(nums)
        if len(tracker)==len(nums):
            return result

        else:

            for key,val in tracker.items():
                if len(val)==1:
                    result[val[0]]=0
                    continue
                preSum=0
                postSum=sum(val)
                val_len=len(val)
                for v in range(val_len):
                    result[val[v]]=abs((val[v]*v)-preSum)+abs((val[v]*(val_len-v-1))-(postSum-preSum-val[v]))
                    preSum+=val[v]

        return result

if __name__ == '__main__':

    obj=Solution()
    print(obj.distance( nums = [1,3,1,1,2]))
    print(obj.distance( nums = [0,5,3]))