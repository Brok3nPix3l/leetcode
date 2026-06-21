from collections import Counter

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c = Counter(costs)
        ice_cream_count = 0
        for cost in sorted(c):
            total_cost = cost * c[cost]
            if coins >= total_cost:
                coins -= total_cost
                ice_cream_count += c[cost]
            else:
                ice_cream_count += coins // cost
                break
        return ice_cream_count