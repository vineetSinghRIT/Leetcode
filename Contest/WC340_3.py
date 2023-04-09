from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0

        nums.sort()

        out=[]

        for i in range(0,len(nums)-1):
            out.append([i,i+1,abs(nums[i+1]-nums[i])])

        out.sort(key=lambda x: x[2])

        if p==1:
            return out[0][2]

        result=[out[0]]
        i=1
        iter=1
        while i<p:
            toC=(result[-1][0],result[-1][0])
            if out[iter][0] not in toC and out[iter][1] not in toC:
                result.append(out[iter])
                i+=1
            iter+=1

        return result[-1][2]

if __name__ == '__main__':
    obj=Solution()
    print(obj.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(obj.minimizeMax(nums = [4,2,1,2], p = 1))
    print(obj.minimizeMax([3,4,2,3,2,1,2],3))