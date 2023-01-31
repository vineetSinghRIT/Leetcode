import math


class Solution:
    def monkeyMove(self, n: int) -> int:
        #num = 2 ** n
        mod=1000000007
        ret=pow(2,n,mod)-2
        return (ret+1000000007)%mod


if __name__ == '__main__':
    obj=Solution()
    print(obj.monkeyMove(3))
    print(obj.monkeyMove(4))
    print(obj.monkeyMove(55))
    print(obj.monkeyMove(500000003))
    print(obj.monkeyMove(996194169))
    print(obj.monkeyMove(599161385))
    print(obj.monkeyMove(993541586))