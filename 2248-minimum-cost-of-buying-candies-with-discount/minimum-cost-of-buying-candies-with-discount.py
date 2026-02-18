class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        cur = 0
        min_cost = 0
        for i, c in enumerate(cost):
            if cur == 2:
                cur = 0
            else:
                cur += 1
                min_cost += c
        return min_cost