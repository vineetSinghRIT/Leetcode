
from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        result = 0
        temp = 0
        i = 0
        mx = 0
        while i < len(books):
            temp += books[i][0]
            mx = max(mx, books[i][1])

            if temp == shelfWidth:
                result += mx
                temp = 0
                mx = 0
                i += 1
                continue

            if temp > shelfWidth:
                i -= 1
                temp = 0
                result += mx
                mx = 0

                continue

            i += 1

        return result

if __name__ == '__main__':
    obj=Solution()
    print(obj.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4))