class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        for i in range(3):
            mat = self.rotate(mat)
            # print(mat)
            if mat == target:
                return True
        
        return False
    
    def rotate(self, mat: List[List[int]]) -> List[List[int]]:
        # 1 2 3
        # 4 5 6
        # 7 8 9
        
        # 7 4 1
        # 8 5 2
        # 9 6 3
        return [list(reversed([(mat[r][c]) for r in range(len(mat))])) for c in range(len(mat[0]))]