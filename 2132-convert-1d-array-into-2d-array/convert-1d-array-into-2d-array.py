class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []
        
        arr_2d = []
        for i in range(m):
            arr_2d.append([])
            for j in range(n):
                # print(f'i={i} j={j} index={i*n+j}')
                arr_2d[i].append(original[i*n+j])
        
        return arr_2d