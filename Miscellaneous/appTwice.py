"""
https://leetcode.com/contest/weekly-contest-303/problems/first-letter-to-appear-twice/
"""

class appTwice:
    def repeatedCharacter(self, s: str) -> str:
        temp=set()
        for c in s:
            if c in temp:
                return c
            else:
                temp.add(c)

if __name__ == '__main__':
    obj=appTwice()
    print(obj.repeatedCharacter("abcdd"))