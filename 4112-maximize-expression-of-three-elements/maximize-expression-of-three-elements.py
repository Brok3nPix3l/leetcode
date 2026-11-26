class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        largest = None
        second_largest = None
        smallest = None

        for num in nums:
            if (largest is None) or (num > largest):
                if second_largest is not None:
                    if smallest is not None:
                        smallest = min(second_largest, smallest)
                    else:
                        smallest = second_largest
                second_largest = largest
                largest = num
            elif (second_largest is None) or (num > second_largest):
                if second_largest is not None:
                    if smallest is not None:
                        smallest = min(second_largest, smallest)
                    else:
                        smallest = second_largest
                second_largest = num
            elif (smallest is None) or (num < smallest):
                smallest = num
            
            # print(f'num={num} largest={largest} second_largest={second_largest} smallest={smallest}')
        
        return largest + second_largest - smallest