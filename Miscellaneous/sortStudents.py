"""
https://leetcode.com/problems/sort-the-students-by-their-kth-score/
"""
from typing import List
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: x[k],reverse=True)
        return score

if __name__ == '__main__':
    obj=Solution()
    print(obj.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2))
    print(obj.sortTheStudents(score = [[3,4],[5,6]], k = 0))