class Solution:
    def countAsterisks(self, s: str) -> int:
        inside_vertical_bars = False
        asterisks = 0
        for c in s:
            if c == '|':
                inside_vertical_bars = not inside_vertical_bars
            elif c == '*' and not inside_vertical_bars:
                asterisks += 1
        return asterisks