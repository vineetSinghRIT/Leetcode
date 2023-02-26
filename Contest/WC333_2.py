import math


class Solution:
    def minOperations(self,n):

        if n==1:
            return 1
        if n == 0:
            return 0
        else:
            pred=self.closest_power_of_2(n)

            if pred<=n:
                return 1+self.minOperations(n-pred)
            else:
                return 1+self.minOperations(pred-n)

    def closest_power_of_2(self,n):
        if n <= 0:
            return 0
        exp = math.floor(math.log2(n))
        lower_power_of_2 = 2 ** exp
        upper_power_of_2 = 2 ** (exp + 1)
        if n - lower_power_of_2 < upper_power_of_2 - n:
            return lower_power_of_2
        else:
            return upper_power_of_2
if __name__ == '__main__':
    obj=Solution()
    print(obj.minOperations(39))
    print(obj.minOperations(54))
    print(obj.minOperations(38))