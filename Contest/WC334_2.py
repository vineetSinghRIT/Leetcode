from typing import List
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        iterLimit=len(word)
        result=[0]*iterLimit
        numR=0
        for i in range(iterLimit):
            numR=numR*10+(int(word[i]))
            if numR%m==0:
                result[i]=1

        return result

if __name__ == '__main__':
    obj=Solution()
    print(obj.divisibilityArray(word = "998244353", m = 3))
    print(obj.divisibilityArray(word = "1010", m = 10))
