class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest = []
        smallest = []
        for num in nums:
            if not largest or num > largest[0]:
                largest.insert(0, num)
            elif len(largest) < 2 or num > largest[1]:
                largest.insert(1, num)
            
            if not smallest or num < smallest[0]:
                smallest.insert(0, num)
            elif len(smallest) < 2 or num < smallest[1]:
                smallest.insert(1, num)
            
            if len(largest) > 2:
                largest.pop()
            if len(smallest) > 2:
                smallest.pop()
        
        return largest[0] * largest[1] - smallest[0] * smallest[1]