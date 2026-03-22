class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid[0]) - 2)]
        for r in range(len(ans)):
            for c in range(len(ans[0])):
                counter = Counter()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        counter[grid[i][j]] += 1
                ans[r][c] = max(counter)
        return ans