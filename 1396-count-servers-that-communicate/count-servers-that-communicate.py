from collections import defaultdict

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        servers_per_row = defaultdict(int)
        servers_per_col = defaultdict(int)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    servers_per_row[i] += 1
                    servers_per_col[j] += 1
        
        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1 and (servers_per_row[i] > 1 or servers_per_col[j] > 1):
                    ans += 1
        
        return ans