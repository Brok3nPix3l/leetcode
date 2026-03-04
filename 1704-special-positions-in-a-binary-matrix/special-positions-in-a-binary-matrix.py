from collections import defaultdict

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        spec_pos = 0
        set_bit_count_by_column = defaultdict(int)
        set_bit_count_by_row = defaultdict(int)
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if cell == 1:
                    set_bit_count_by_column[c] += 1
                    set_bit_count_by_row[r] += 1
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if cell == 1:
                    if set_bit_count_by_column[c] == 1 and set_bit_count_by_row[r] == 1:
                        spec_pos += 1
        return spec_pos