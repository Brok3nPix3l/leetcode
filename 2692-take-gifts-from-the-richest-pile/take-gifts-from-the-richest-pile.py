import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        ans = 0
        for _ in range(k):
            cur = heapq.heappop_max(gifts)
            if cur == 1:
                ans += 1
                break
            cur = floor(sqrt(cur))
            heapq.heappush_max(gifts, cur)
        for gift in gifts:
            ans += gift
        return ans