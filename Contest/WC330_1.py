class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n==1 else n-1

if __name__ == '__main__':
    obj=Solution()
    print(obj.distinctIntegers(5))