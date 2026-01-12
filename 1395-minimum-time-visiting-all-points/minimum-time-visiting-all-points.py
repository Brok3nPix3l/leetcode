class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Moving from point a to point b takes max(abs(y1-y2),abs(x1-x2)) time
        Iterate over all points, determining how long it takes to move between them and adding to a counter
        Return final value of counter
        """
        time = 0
        for i, point in enumerate(points[:-1]):
            time += max(abs(points[i + 1][0] - point[0]), abs(points[i + 1][1] - point[1]))

        return time
