from math import sqrt, floor

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(num: int) -> int:
            divisors = set()
            divisors.add(1)
            divisors.add(num)
            for i in range(2, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
            # print(num, divisors)
            return list(divisors)
        
        sum_divisors = 0
        for num in nums:
            d = divisors(num)
            if len(d) == 4:
                sum_divisors += sum(d)
        return sum_divisors