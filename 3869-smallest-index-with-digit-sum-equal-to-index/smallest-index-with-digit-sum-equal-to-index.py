class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(digits(num)) == i:
                return i
        
        return -1

def digits(num: int) -> List[int]:
    if num == 0:
        return [0]
    
    ans = []

    while num > 0:
        ans.append(num % 10)
        num //= 10
    
    return ans