"""
https://leetcode.com/problems/valid-anagram/
"""
class anaGram:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS=len(s)
        lenT=len(t)
        dictS=dict()
        for char in s:
            if char in dictS:
                dictS[char]+=1
            else:
                dictS[char]=1

        if lenS!=lenT:
            return False

        for char in t:
            if char in dictS.keys() and dictS[char]>0:
                dictS[char]-=1
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    obj=anaGram()
    s="a"
    t="a"
    ans=obj.isAnagram(s,t)
    print(ans)