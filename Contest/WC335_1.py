class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q=time//(n-1)
        r=time%(n-1)
        if q==0 or q%2==0:
            return r+1
        else:
            return n-r

if __name__ == '__main__':
    obj=Solution()
    print(obj.passThePillow( n = 4, time = 5))
    print(obj.passThePillow( n = 3, time = 2))
    print(obj.passThePillow( n = 2, time = 1))
