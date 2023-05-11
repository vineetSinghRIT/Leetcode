class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       return self.helper(n,n,"",[])


    def helper(self,open,close,temp,finalL):
        if open==0:
            temp+=')'*close
            finalL.append(temp)
            return finalL

        if open>0 and close==0:
            return finalL
        if open>close:
            return finalL

        finalL=self.helper(open-1,close,temp+"(",finalL)
        finalL=self.helper(open,close-1,temp+")",finalL)

        return finalL