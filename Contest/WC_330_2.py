import math


class Solution:
    def monkeyMove(self, n: int) -> int:
        #num = 2 ** n

        result = 1
        x=2
        while (n > 0):
            if (n % 2 == 0):
                x = x * x
                n = n / 2

            else:
                result = result * x
                n = n - 1

            if result>(10 ** 9 + 7):
                result=result%(10 ** 9 + 7)
        result -= 2

        if result > 0:
            return result
        else:
            return result + 1000000007


if __name__ == '__main__':
    obj=Solution()
    print(obj.monkeyMove(3))
    print(obj.monkeyMove(4))
    print(obj.monkeyMove(55))
    print(obj.monkeyMove(500000003))
    print(obj.monkeyMove(996194169))
    print(obj.monkeyMove(599161385))
    print(obj.monkeyMove(993541586))