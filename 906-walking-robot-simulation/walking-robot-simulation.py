class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(tuple(o) for o in obstacles)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        cur_pos = (0, 0)
        max_dist = 0
        for c in commands:
            if c == -2:
                cur_dir = (cur_dir - 1) % len(dirs)
            elif c == -1:
                cur_dir = (cur_dir + 1) % len(dirs)
            else:
                for i in range(c):
                    new_pos = (cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1])
                    if new_pos not in obstacle_set:
                        cur_pos = new_pos
                        cur_dist = abs(cur_pos[0]) ** 2 + abs(cur_pos[1]) ** 2
                        max_dist = max(max_dist, cur_dist)
        return max_dist