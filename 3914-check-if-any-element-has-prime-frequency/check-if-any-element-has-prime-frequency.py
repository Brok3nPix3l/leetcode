import functools
from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # for i in range(10):
        #     print(f'{i} -> {'prime' if isPrime(i) else 'not prime'}')
        return any(isPrime(freq) for freq in sorted(Counter(nums).values()))

@cache
def isPrime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    
    return True