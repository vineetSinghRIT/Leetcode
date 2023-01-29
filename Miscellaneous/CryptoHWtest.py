class crypto:
    def getFreq(self,strg):
        tracker=dict()
        for c in strg:
            tracker[c]=tracker.get(c,0)+1
        return tracker
    def repBy(self,strg,org,rep):
        return strg.replace(org,rep)

    def shiftCyper(self,inputString,k):
        temp=""
        for c in inputString:
            temp+=chr((((ord(c) - 96)+k)%26)+96)
        return temp

if __name__ == '__main__':
    obj=crypto()
    initial="nybfxymjgjxytkynrjxnybfxymjbtwxytkynrjxnybfxymjfljtkbnxitrnybfxymjfljtkkttqnxmsjxx"

    #Prints Frequency of each character in input string
    print(obj.getFreq(initial))

    #Prints Shifted text
    print(obj.shiftCyper(initial,-5))

    #Prints orginal test
    print(initial)