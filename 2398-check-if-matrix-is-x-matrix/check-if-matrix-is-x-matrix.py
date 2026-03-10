class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                # print(f'i={i} j={j} cell={cell}')
                if i == j or i + j == len(grid) - 1:
                    if cell == 0:
                        return False
                elif cell != 0:
                    return False
        return True