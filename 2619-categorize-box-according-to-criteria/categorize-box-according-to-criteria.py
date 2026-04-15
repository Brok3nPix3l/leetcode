class Solution:
    BULKY_DIMENSION_SIZE = 10 ** 4
    BULKY_VOLUME = 10 ** 9

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        isBulky = (
            any(dimension >= self.BULKY_DIMENSION_SIZE for dimension in (length, width, height))
            or volume >= self.BULKY_VOLUME
        )
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return 'Both'
        elif isBulky:
            return 'Bulky'
        elif isHeavy:
            return 'Heavy'
        else:
            return 'Neither'