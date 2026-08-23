class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.sumOfSquaresOfDigits(n)
        return True
    
    def sumOfSquaresOfDigits(_, n: int) -> int:
        originalN = n
        # print('sumOfSquaresOfDigits', 'n', n)
        ans = 0
        while n > 0:
            digit = n % 10
            square = digit ** 2
            ans += square
            # print('sumOfSquaresOfDigits', 'digit', digit, 'square', square, 'ans', ans)
            n //= 10
        # print('sumOfSquaresOfDigits', originalN, '->', ans)
        return ans