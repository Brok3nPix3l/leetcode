class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = []
        queue.append(start)
        while queue:
            cur = queue.pop(0)
            if arr[cur] == 0:
                return True
            if cur in visited:
                continue
            visited.add(cur)

            possible_idxs = [cur + arr[cur], cur - arr[cur]]
            for p in possible_idxs:
                if p >= 0 and p < len(arr):
                    queue.append(p)
        return False