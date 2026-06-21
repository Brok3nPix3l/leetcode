class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # first 5 liters come from mainTank before 1 liter added from additionalTank
        # then for every 4 liters in mainTank, 1 liter is added from additionalTank
        if mainTank < 5:
            return mainTank * 10
        return (min(additionalTank - 1, (mainTank - 5) // 4) + mainTank + 1) * 10