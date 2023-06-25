class Solution:
    def smallestString(self, s: str) -> str:
        beg=0
        end=len(s)

        checkCase=set(list(s))

        if s[0]=='a' and len(checkCase)==1:
            return s[0:len(s)-1]+'z'

        for i in range(len(s)):
            if s[i]!='a':
                beg=i
                break

        for j in range(len(s)-1,-1,-1):
            if s[j]=='a':
                end=j
            if beg>=j:
                break

        if end==len(s):
            return s[0:beg] + self.helper(s[beg:end])
        elif beg==0:
            return self.helper(s[beg:end])+s[end:len(s)]
        else:
            return s[0:beg]+self.helper(s[beg:end])+s[end:len(s)]

    def helper(self,word):
        shifted_s = []
        for c in word:
            if c == 'a':
                shifted_s.append('z')
            else:
                shifted_s.append(chr(ord(c) - 1))
        return ''.join(shifted_s)


if __name__ == '__main__':
    obj=Solution()
    print(obj.smallestString("cbabc"))
    print(obj.smallestString("acbbc"))
    print(obj.smallestString(s = "leetcode"))
    print(obj.smallestString(s = "aa"))
    print(obj.smallestString(s = "a"))
    print(obj.smallestString(s = "ab"))
    print(obj.smallestString(s = "ba"))
    print(obj.smallestString(s = "bb"))
    print(obj.smallestString(s = "b"))
    print(obj.smallestString(s = "z"))

