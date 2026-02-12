class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i+1])
            rods[rod].add(color)
        rods_with_all_rings = [rod for rod in rods if len(rod) == 3]
        # print(rods_with_all_rings)
        return len(rods_with_all_rings)