"""
https://leetcode.com/problems/island-perimeter/description/
"""
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    result+=self.getPer(i,j,grid)

        return result

    def getPer(self,i,j,grid):

        incr=[(1,0),(-1,0),(0,1),(0,-1)]
        temp=0
        for dx,dy in incr:
            stepX=i+dx
            stepY=j+dy
            if stepX<0 or stepX>=len(grid) or stepY<0 or stepY>=len(grid[0]):
                temp+=1
            elif grid[stepX][stepY]==0:
                temp+=1
            else:
                temp+=0

        return temp

if __name__ == '__main__':
    obj=Solution()
    print(obj.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(obj.islandPerimeter(grid = [[1]]))
    print(obj.islandPerimeter(grid = [[1,0]]))
