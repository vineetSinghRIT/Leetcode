class Solution:
    def punishmentNumber(self, n: int) -> int:
        result=0
        for i in range(37,n+1):
            if self.isValid(i):
                result+=i**2
        return result

    def isValid(self,n):
        n_sqr=n*n
        n_sqr=str(n_sqr)
        all_possible_parts=self.allpartitions(n_sqr,0,len(n_sqr))

        for partition in all_possible_parts:
            if sum(partition) == n:
                return True
        return False

    def allpartitions(self,num_str, start, end):
        if start == end-1:
            return [[int(num_str[start])]]
        partitions = []
        for i in range(start, end):
            left = int(num_str[start:i+1])
            check=self.allpartitions(num_str, i+1, end)
            if len(check)==0:
                partitions.append([left])
            for right_partition in check:
                partitions.append([left] + right_partition)
        return partitions


if __name__ == '__main__':
    obj=Solution()
    #print(obj.punishmentNumber(10))
    #print(obj.punishmentNumber(37))
    print(obj.punishmentNumber(45))


# Input:
# 45
# Output:
# 1478
# Expected:
# 3503
