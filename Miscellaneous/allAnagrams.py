"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from collections import Counter


class allAnagrams:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        cnt = Counter(p)

        ans = []
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:  # If number of characters `c` is more than our expectation
                cnt[s[l]] += 1  # Slide left until cnt[c] == 0
                l += 1
            temp=r - l + 1
            if r - l + 1 == len(p):  # If we already filled enough `p.length()` chars
                ans.append(l)  # Add left index `l` to our result

        return ans
    def findAnagrams2(self, s: str, p: str) -> list[int]:
        lenp = len(p)
        dictP = self.genDict(p)
        total = []

        for i in range(len(s) - lenp + 1):

            if s[i] in dictP:
                if i > 0 and i - 1 in total and s[i + lenp - 1] == s[i - 1]:
                    total.append(i)

                else:
                    wordinS = self.genDict(s[i:i + lenp])
                    if self.compareDict(dictP, wordinS):
                        total.append(i)

        return total

    def genDict(self, s):
        dictS = dict()
        for char in s:
            if char in dictS:
                dictS[char] += 1
            else:
                dictS[char] = 1
        return dictS

    def compareDict(self, d1, d2):

        for key, value in d1.items():
            if key not in d2:
                return False

            if d2[key] != value:
                return False

        return True
if __name__ == '__main__':
    obj=allAnagrams()
    print(obj.findAnagrams("cbaebabacd","abc"))
    print(obj.findAnagrams("abab","ab"))
