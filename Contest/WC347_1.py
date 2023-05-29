class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        while True:
            if len(num)==0:
                return ""
            if num[-1] == '0':
                num = num[:-1]
            else:
                return num

if __name__ == '__main__':
    obj=Solution()
    print(obj.removeTrailingZeros("51230100"))
    print(obj.removeTrailingZeros("000"))
    print(obj.removeTrailingZeros("31514216007864075756059111751787923413952537015859352242147727420"))