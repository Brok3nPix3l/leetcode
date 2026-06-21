class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        freq = [0] * (mx + 1)
        for cost in costs:
            freq[cost] += 1
        ice_cream_count = 0
        for cost, f in enumerate(freq):
            if f == 0:
                continue
            total_cost = cost * f
            if coins >= total_cost:
                coins -= total_cost
                ice_cream_count += f
            else:
                ice_cream_count += coins // cost
                break
        return ice_cream_count