from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_by_value = defaultdict(list[int])
        for i, v in enumerate(nums):
            index_by_value[v].append(i)
        # print(index_by_value)
        ans = 0
        for num, idxs in index_by_value.items():
            if len(idxs) < 2:
                continue
            # print(idxs)
            for i in range(len(idxs)):
                for j in range(i+1, len(idxs)):
                    if idxs[i] * idxs[j] % k == 0:
                        # print(f'i={i} j={j}')
                        ans += 1
        return ans