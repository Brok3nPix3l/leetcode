class Solution:
    MIN_Y = 0
    MAX_Y = 10 ** 9
    THETA = 10 ** -5
    
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        binary search with real numbers
        if (the area above the line) - (the area below the line) <= theta, return that line
        to determine the area above/below a given line:
            brute force:
            iterate over each square in the list
            compute the parts of the square (rectangles) that are above/below the line and add those values to their respective count (might be the entire square / none of the square / part of the square)
        """
        
        l = self.MIN_Y
        r = self.MAX_Y
        while r - l > self.THETA:
            m = (l + r) / 2.0
            # print(f'l={l} m={m} r={r}')
            area_above_line, area_below_line = self.area_above_and_below_line(m, squares)
            # print(f'area_above_line={area_above_line} area_below_line={area_below_line}')
            # if abs(area_above_line - area_below_line) <= THETA:
            #     return m
            if area_below_line < area_above_line:
                # line is too low
                l = m
                # print(f'l={l}')
            else:
                # line is too high
                r = m
                # print(f'r={r}')
        
        return l
    
    def area_above_and_below_line(self, line: float, squares: List[List[int]]) -> Tuple[float, float]:
        area_above_line = 0
        area_below_line = 0

        for square in squares:
            if square[1] > line:
                # square is fully above line
                area_above_line += square[2] ** 2
            elif square[1] + square[2] < line:
                # square is fully below line:
                area_below_line += square[2] ** 2
            else:
                # square intersects line
                area_above_line += (square[1] + square[2] - line) * square[2]
                area_below_line += (line - square[1]) * square[2]

        return (area_above_line, area_below_line)