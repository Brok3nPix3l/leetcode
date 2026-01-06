class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def is_valid_point(point: List[int], x: int, y: int) -> bool:
            return point[0] == x or point[1] == y
        
        def manhattan_distance(point_a: List[int], point_b: List[int]) -> int:
            return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
        
        nearest_point_index = -1
        nearest_point_distance = None
        for index, point in enumerate(points):
            if not is_valid_point(point, x, y):
                continue
            point_distance = manhattan_distance([x, y], point)
            if nearest_point_distance is None or point_distance < nearest_point_distance:
                # print(f'new closest point {index}: {point} with distance {point_distance}')
                nearest_point_distance = point_distance
                nearest_point_index = index
        
        return nearest_point_index