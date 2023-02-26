from typing import  List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        x,y=0,0
        merge=[]
        while x<len(nums1) and y<len(nums2):

            if nums1[x][0]==nums2[y][0]:
                merge.append([nums1[x][0],nums1[x][1]+nums2[y][1]])
                x+=1
                y+=1
            elif nums1[x][0]>nums2[y][0]:
                merge.append(nums2[y])
                y+=1
            else:
                merge.append(nums1[x])
                x+=1

        merge+=nums1[x:]+nums2[y:]
        return merge

if __name__ == '__main__':
    obj=Solution()
    print(obj.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))
    print(obj.mergeArrays(nums1 = [[1,1]], nums2 = [[1,1]]))
    print(obj.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))





