class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        if c['L'] > c['R']:
            return c['L'] + c['_'] - c['R']
        return c['R'] + c['_'] - c['L']