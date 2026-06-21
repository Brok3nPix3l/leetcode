from collections import Counter

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c = Counter(costs)
        ice_cream_count = 0
        for cost in sorted(c):
            freq = c[cost]
            if freq == 0:
                continue
            total_cost = cost * freq
            if coins >= total_cost:
                coins -= total_cost
                ice_cream_count += freq
            else:
                ice_cream_count += coins // cost
                break
        return ice_cream_count