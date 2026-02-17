class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [set() for _ in matrix]
        cols = [set() for _ in matrix[0]]
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                # if cell in rows[r] or cell in cols[c]:
                #     return False
                rows[r].add(cell)
                cols[c].add(cell)
        for row in rows:
            if len(row) < n:
                return False
        for col in cols:
            if len(col) < n:
                return False
        return True