
from typing import List
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        result = 0

        for i in range(len(nums)):
            diag=nums[i][i]
            n_diag=nums[i][len(nums) - i - 1]
            if self.is_prime(diag) and diag>result:
                result=diag
            if self.is_prime(n_diag) and n_diag > result:
                result = n_diag

        return result

    def is_prime(self,n):
        if n <= 1:
            return False
        sqt=int(n ** 0.5) + 1
        for i in range(2, sqt):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    obj=Solution()
    print(obj.diagonalPrime(nums = [[1,2,3],[5,17,7],[9,11,10]]))
    print(obj.diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]]))
    print(obj.diagonalPrime(nums = [[1]]))