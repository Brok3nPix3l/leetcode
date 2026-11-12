import heapq

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        top_k = []

        for num in nums:
            if num in top_k:
                continue
            
            if len(top_k) >= k:
                heapq.heappushpop(top_k, num)
            else:
                heapq.heappush(top_k, num)
        
        return sorted(top_k, reverse=True)