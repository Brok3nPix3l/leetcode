class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest, largest = self.smallest_and_largest(nums)
        
        return self.gcd(smallest, largest)

    def smallest_and_largest(self, nums: list[nums]) -> tuple[int, int]:
        smallest = None
        largest = None
        for n in nums:
            if not smallest or n < smallest:
                smallest = n
            if not largest or n > largest:
                largest = n
        
        return (smallest, largest)

    def gcd(self, n1, n2):
        if n1 == 0:
            return n2
        
        return gcd(n2 % n1, n1)