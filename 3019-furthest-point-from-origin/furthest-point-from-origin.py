class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        return abs(c.get('L', 0) - c.get('R', 0)) + c['_']