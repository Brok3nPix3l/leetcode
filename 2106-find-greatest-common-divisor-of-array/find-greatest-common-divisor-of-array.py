import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest, largest = self.smallest_and_largest(nums)
        
        return math.gcd(smallest, largest)

    def smallest_and_largest(self, nums: list[nums]) -> tuple[int, int]:
        smallest = None
        largest = None
        for n in nums:
            if smallest == None or n < smallest:
                smallest = n
            if largest == None or n > largest:
                largest = n
        
        return (smallest, largest)