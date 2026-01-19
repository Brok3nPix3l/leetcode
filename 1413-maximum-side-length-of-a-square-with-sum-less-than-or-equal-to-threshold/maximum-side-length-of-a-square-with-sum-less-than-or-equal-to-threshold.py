import math

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix_sum = []
        for row in mat:
            prefix_sum_row = []
            cur = 0
            for cell in row:
                cur += cell
                prefix_sum_row.append(cur)

            prefix_sum.append(prefix_sum_row)

        l = 0
        r = min(len(mat), len(mat[0]))
        while l < r:
            m = math.ceil((l + r) / 2)
            # print(f'm={m}')
            if self.valid_square_exists(m, prefix_sum, mat, threshold):
                l = m
            else:
                r = m - 1
        
        return l
    
    def valid_square_exists(self, square_side_length: int, prefix_sum: list[list[int]], mat: list[list[int]], threshold: int) -> bool:
        for i in range(len(mat)):
            if len(mat) < i + square_side_length:
                continue
            for j in range(len(mat[0])):
                if len(mat[0]) < j + square_side_length:
                    continue
                # print(f'i={i} j={j}')
                if self.is_valid_square(i, j, square_side_length, prefix_sum, mat, threshold):
                    # print(f'valid square exists at i={i} j={j}')
                    return True
        
        return False
    
    def is_valid_square(self, i: int, j: int, square_side_length: int, prefix_sum: list[list[int]], mat: list[list[int]], threshold: int) -> bool:
        return sum([(prefix_sum[a][j+square_side_length-1]-(prefix_sum[a][j-1] if j > 0 else 0)) for a in range(i, i+square_side_length)]) <= threshold