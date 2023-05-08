from typing import List
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        toPaint=[0]*(n+2)
        result=[0]*(len(queries)+1)
        for i in range(len(queries)):
            index,color =queries[i]
            if toPaint[index+1]==0:
                if toPaint[index]==color or toPaint[index+2]==color:
                    tot=result[i]
                    if toPaint[index]==color:
                        tot+=1
                    if toPaint[index+2]==color:
                        tot += 1
                    result[i+1]=tot
                else:
                    result[i + 1]=result[i]
            else:

                if toPaint[index + 1]!=color:
                    tot=result[i]
                    if toPaint[index + 1]==toPaint[index]:
                        tot-=1
                    elif toPaint[index]==color:
                        tot+=1
                    if toPaint[index + 1]==toPaint[index+2]:
                        tot-=1
                    elif toPaint[index+2]==color:
                        tot+=1
                    result[i +1] = tot
                else:
                    result[i + 1] = result[i]
                    continue


            toPaint[index+1]=color


        return result[1:]


if __name__ == '__main__':
    obj=Solution()
    #print(obj.colorTheArray(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]))
    #print(obj.colorTheArray(n = 1, queries = [[0,100000]]))
    print(obj.colorTheArray(18,[[9,5],[14,15],[8,14],[0,4],[10,19],[13,11],[11,18],[8,15],[17,9],[10,1],
                                [17,8],[9,13],[2,17],[0,10],[10,15],[10,19],[1,13],[7,1],[2,7],[13,16],
                                [2,12],[1,19],[0,9],[4,1],[1,7],[3,18],[10,7],[13,2],[13,9],[0,17],
                                [14,11],[12,7],[12,18],[16,15],
                                [16,13],[7,12],[15,12],[7,18],[15,16],[15,6]]))