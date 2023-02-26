from typing import List
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        iterLimit=len(word)
        result=[0]*iterLimit
        numR=0
        for i in range(iterLimit):
            numR=(numR*10+(int(word[i])))%m
            if numR==0:
                result[i]=1

        return result