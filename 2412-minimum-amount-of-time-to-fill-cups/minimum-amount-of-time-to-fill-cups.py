import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heapq.heapify_max(amount)
        time = 0
        while amount[0] > 0:
            time += 1
            largest = heapq.heappop_max(amount)
            second_largest = heapq.heappop_max(amount)
            largest -= 1
            if second_largest > 0:
                second_largest -= 1
            heapq.heappush_max(amount, largest)
            heapq.heappush_max(amount, second_largest)
        return time