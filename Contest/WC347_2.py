from typing import List
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        result=[[0]*len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                topLeft=self.getTL(grid,r,c)
                botRight=self.getBR(grid,r,c)
                result[r][c]=abs(len(set(topLeft))-len(set(botRight)))
        return result

    def getTL(self,grid,r,c):
        if r-1<0 or c-1<0:
            return []
        else:
            return [grid[r-1][c-1]]+self.getTL(grid,r-1,c-1)

    def getBR(self,grid,r,c):
        if r+1>=len(grid) or c+1>=len(grid[0]):
            return []
        else:
            return [grid[r+1][c+1]]+self.getBR(grid,r+1,c+1)

if __name__ == '__main__':
    obj=Solution()
    print(obj.differenceOfDistinctValues( [[1,2,3],[3,1,5],[3,2,1]]))
    print(obj.differenceOfDistinctValues( [[1]]))
    print(obj.differenceOfDistinctValues( [[6,28,37,34,12,30,43,35,6],[21,47,38,14,31,49,11,14,49],[6,12,35,17,17,2,45,27,43],[34,41,30,28,45,24,50,20,4]]))

