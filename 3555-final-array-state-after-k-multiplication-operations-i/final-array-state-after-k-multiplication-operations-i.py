import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numsWithIndex = [(n, i) for i, n in enumerate(nums)]

        heapq.heapify(numsWithIndex)
        
        for _ in range(k):
            n, i = heapq.heappop(numsWithIndex)
            new = (n * multiplier, i)
            heapq.heappush(numsWithIndex, new)
        
        numsInIndexOrder = sorted(numsWithIndex, key=lambda a: a[1])

        ans = list(map(lambda a: a[0], numsInIndexOrder))
        
        return ans