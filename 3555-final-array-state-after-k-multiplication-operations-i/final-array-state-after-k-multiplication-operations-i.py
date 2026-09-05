import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numsWithIndex = [(n, i) for i, n in enumerate(nums)]

        heapq.heapify(numsWithIndex)
        
        for _ in range(k):
            n, i = heapq.heappop(numsWithIndex)
            n *= multiplier
            nums[i] = n
            heapq.heappush(numsWithIndex, (n, i))
        
        return nums