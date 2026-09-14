class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        class Rectangle:
            def __init__(self, coords):
                self.x1, self.y1, self.x2, self.y2 = coords
            
            def __str__(self):
                return f'({self.x1}, {self.y1}) ({self.x2}, {self.y2})'

        r1 = Rectangle(rec1)
        r2 = Rectangle(rec2)

        return not (
            r1.x2 <= r2.x1 or \
            r2.x2 <= r1.x1 or \
            r1.y2 <= r2.y1 or \
            r2.y2 <= r1.y1)