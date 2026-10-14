class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        nines = sum // 9
        rem = sum % 9

        # print(f'nines={nines} rem={rem}')
        if rem > 0:
            if nines + 1 > num:
                return ""
            return '9' * nines + str(rem) + '0' * (num - nines - 1)
        else:
            if nines > num:
                return ""
            return '9' * nines + '0' * (num - nines)