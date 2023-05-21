class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        end=len(s)//2
        result=list(s)
        for i in range(end):
            right=len(s)-1-i
            if s[i]!=s[right]:
                if ord(s[i])<ord(s[right]):
                    result[right]=s[i]
                else:
                    result[i] = s[right]
        return ''.join(result)

if __name__ == '__main__':
    obj=Solution()
    print(obj.makeSmallestPalindrome(s = "egcfe"))
    print(obj.makeSmallestPalindrome("abcd"))
    print(obj.makeSmallestPalindrome("seven"))