class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        above = 0
        below = sum(sum(cell for cell in row) for row in grid)
        left = 0
        right = below
        for row in grid:
            above += sum(row)
            below -= sum(row)
            if above == below:
                return True
        
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                left += grid[r][c]
                right -= grid[r][c]
                if left == right:
                    return True
        
        return False