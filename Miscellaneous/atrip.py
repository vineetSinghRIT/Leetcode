class atrip:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:

        diffArry=[0]*201

        for num in nums:
            diffArry[num]=1

        output=0
        for num in nums:
            if (num+diff)<=200 and diffArry[num+diff]==1 and (num+(2*diff))<=200 and diffArry[num+(2*diff)]==1:
                output+=1

        return output


if __name__ == '__main__':
    obj=atrip()
    print(obj.arithmeticTriplets([0,1,4,6,7,10], 3))



