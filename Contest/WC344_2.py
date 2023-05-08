class FrequencyTracker:

    def __init__(self):
        self.tracker=defaultdict(int)
        self.invFreq = defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.tracker:
            self.invFreq[self.tracker[number]]-=1
            self.tracker[number]+=1
            self.invFreq[self.tracker[number]] += 1
        else:
            self.tracker[number] = 1
            self.invFreq[1] += 1

    def deleteOne(self, number: int) -> None:

        if number in self.tracker:
            if self.tracker[number]==0:
                return None
            else:
                self.invFreq[self.tracker[number]] -= 1
                self.tracker[number] -= 1
                self.invFreq[self.tracker[number]] += 1
        else:
            return None

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.invFreq and self.invFreq[frequency]>0:
            return True
        else:
            return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
Console
