import math

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 > xCenter:
            # rectangle is to the right of circle
            closestX = x1
        elif x2 < xCenter:
            # rectangle is to the left of circle
            closestX = x2
        else:
            # rectangle has horizontal overlap with circle
            closestX = xCenter
        
        if y1 > yCenter:
            # rectangle is above circle
            closestY = y1
        elif y2 < yCenter:
            # rectangle is below circle
            closestY = y2
        else:
            # rectangle has vertical overlap with circle
            closestY = yCenter
        
        return abs(distance((closestX, closestY), (xCenter, yCenter))) <= radius

def distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)