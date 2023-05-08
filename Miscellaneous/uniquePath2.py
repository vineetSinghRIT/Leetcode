from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        if len(obstacleGrid)==1 and len(obstacleGrid[0])==1:
            if obstacleGrid[0][0]==0:
                return 1
            else:
                return 0

        tracker=dict()


        def helper(x,y,grid):
            if x==len(grid) or y==len(grid[0]) or grid[x][y]==1:
                return 0
            if (x==len(grid)-1 and y==len(grid[0])-1):
                return 1
            if (x,y) in tracker:
                return tracker[(x,y)]

            right=helper(x+1,y,grid)
            down=helper(x,y+1,grid)
            tracker[(x,y)]=right+down
            return tracker[(x,y)]

        helper(0, 0, obstacleGrid)
        return tracker[(0, 0)]

if __name__ == '__main__':
    obj=Solution()
    print(obj.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
    print(obj.uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]]))
    print(obj.uniquePathsWithObstacles(obstacleGrid = [[0]]))
    print(obj.uniquePathsWithObstacles(obstacleGrid = [[1]]))
    print(obj.uniquePathsWithObstacles(obstacleGrid = [[0,1]]))