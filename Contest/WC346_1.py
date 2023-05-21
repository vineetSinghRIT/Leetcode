class Solution:
    def minLength(self, s: str) -> int:
        i=0
        while True:
            if i==len(s)-1 or len(s)<2:
                break
            else:
                if s[i:i+2] in ["AB","CD"]:
                    s=s[:i]+s[i+2:]
                    i=0
                else:
                    i+=1

        return len(s)

if __name__ == '__main__':
    obj=Solution()
    print(obj.minLength("ABFCACDB"))
    print(obj.minLength("ACBBD"))
    print(obj.minLength("A"))
