from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(int)
        for item in items1:
            ans[item[0]] += item[1]
        for item in items2:
            ans[item[0]] += item[1]
        return sorted([[item[0], item[1]] for item in ans.items()])