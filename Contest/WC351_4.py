
"""
https://github.com/qiqi-impact/cp/blob/master/leetcode-contest/weekly-351/4.py
"""

from typing import List
class Solution:
    def survivedRobotsHealths(self, p: List[int], h: List[int], d: str) -> List[int]:
        n = len(p)
        pp = sorted(list(range(n)), key=lambda x:p[x])
        st = []
        for i in pp:
            if d[i] == 'R':
                st.append(i)
            else:
                while st and h[i]:
                    a = 0 if h[st[-1]] <= h[i] else h[st[-1]]-1
                    b = 0 if h[st[-1]] >= h[i] else h[i]-1
                    h[st[-1]] = a
                    h[i] = b
                    if st and h[st[-1]] == 0:
                        st.pop()
        return [x for x in h if x != 0]


if __name__ == '__main__':
    obj=Solution()
    print(obj.survivedRobotsHealths([3,5,2,6],[10,10,15,12],"RLRL"))