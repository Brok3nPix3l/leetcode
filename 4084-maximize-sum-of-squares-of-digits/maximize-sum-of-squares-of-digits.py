class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        nines = sum // 9
        rem = sum % 9

        # print(f'nines={nines} rem={rem}')
        ans = '9' * nines
        if rem > 0:
            if nines + 1 > num:
                return ""
            ans += str(rem) + '0' * (num - nines - 1)
        else:
            if nines > num:
                return ""
            ans += '0' * (num - nines)
        
        return ans