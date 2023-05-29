class Solution:
    def minimumCost(self, s: str) -> int:
        cost=0

        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                cost+=min(i,len(s)-i)

        return cost

if __name__ == '__main__':
    obj=Solution()
    print(obj.minimumCost("0011"))
    print(obj.minimumCost("010101"))
