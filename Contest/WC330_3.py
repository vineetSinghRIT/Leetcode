class Solution:
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        v, d = [0] * (len(weights) - 1), 0
        for i in range(len(weights) - 1):
            v[i] = weights[i] + weights[i + 1]
        v.sort()
        for i in range(k - 1):
            d += v[len(weights) - 2 - i] - v[i]
        return d

if __name__ == '__main__':
    obj=Solution()
    print(obj.putMarbles(weights = [1,3,5,1], k = 2))