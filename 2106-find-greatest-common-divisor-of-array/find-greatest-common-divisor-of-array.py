class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = None
        largest = None
        for n in nums:
            if not smallest or n < smallest:
                smallest = n
            if not largest or n > largest:
                largest = n
        
        for i in range(smallest, 1, -1):
            if largest % i == 0 and smallest % i == 0:
                return i
        
        return 1