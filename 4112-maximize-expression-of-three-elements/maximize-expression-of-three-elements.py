class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        largest = -float('inf')
        second_largest = -float('inf')
        smallest = float('inf')

        for num in nums:
            if num > largest:
                if second_largest != -float('inf'):
                    smallest = min(second_largest, smallest)
                second_largest = largest
                largest = num
            elif num > second_largest:
                if second_largest != -float('inf'):
                    smallest = min(second_largest, smallest)
                second_largest = num
            elif num < smallest:
                smallest = num
            
            # print(f'num={num} largest={largest} second_largest={second_largest} smallest={smallest}')
        
        return largest + second_largest - smallest