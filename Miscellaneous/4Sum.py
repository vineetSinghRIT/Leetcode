"""
https://leetcode.com/problems/4sum-ii/
"""
class FourSum:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        return self.helper(nums1,nums2,nums3,nums4)

    def helper(self,l1,l2,l3,l4):
        firstD=dict()
        secondD=dict()
        n=len(l1)
        for i in range(n):
            for j in range(n):
                if (l1[i] + l2[j]) in firstD.keys():
                    firstD[l1[i] + l2[j]] += 1
                else:
                    firstD[l1[i] + l2[j]] = 1

                if (l3[i] + l4[j]) in secondD.keys():
                    secondD[l3[i] + l4[j]]+=1
                else:
                    secondD[l3[i] + l4[j]] = 1


        count=0
        for key1,val1 in firstD.items():
                if 0-key1 in secondD.keys():
                    count+=val1*secondD[0-key1]

        return count


if __name__ == '__main__':
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]

    obj=FourSum()
    print(obj.fourSumCount(nums1,nums2,nums3,nums4))
