class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            if self.is_prime(len(bin(i)[2:].replace('0', ''))):
                ans += 1
        return ans

    def is_prime(self, num: int) -> bool:
        # print(f'is_prime {num}')
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        ans = True
        for i in range(2, ceil(sqrt(num)) + 1):
            # print(f'i={i}')
            if num % i == 0:
                ans = False
                break
        # print(f'{num} {ans}')
        return ans