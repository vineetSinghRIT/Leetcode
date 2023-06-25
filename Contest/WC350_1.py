class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int: \
        result = 0
        while mainTank > 0:
            if mainTank >= 5 and additionalTank > 0:
                mainTank -= 4
                additionalTank -= 1
                result += 50

            else:
                result += (mainTank * 10)
                return result