from typing import List
import numpy as np
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_dict=dict()
        col_dict=dict()
        apply=[]

        for i in range(len(queries)-1,-1,-1):

            ele=queries[i]

            if ele[0]==0:
                if ele[1] not in row_dict:
                    row_dict[ele[1]]=1
                    apply.append(ele)
            else:
                if ele[1] not in col_dict:
                    col_dict[ele[1]]=1
                    apply.append(ele)
            check=sum(row_dict.values())+sum(col_dict.values())
            if check==(2*n):
                break

        amat = np.zeros((n, n))

        for i in range(len(apply)-1,-1,-1):
            action=apply[i]
            if action[0]==0:
                amat[action[1]]=[action[2]]*n
            else:
                amat[:,action[1]] = [action[2]]*n

        result=np.sum(amat)
        return int(result)

if __name__ == '__main__':
    obj=Solution()
    print(obj.matrixSumQueries(n=3, queries=[[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]))
    print(obj.matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))





