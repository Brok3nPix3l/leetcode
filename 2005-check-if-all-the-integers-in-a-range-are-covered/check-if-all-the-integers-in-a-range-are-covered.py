class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])
        cur_range = 0
        for t in range(left, right + 1):
            # print(t)
            found = False
            while cur_range < len(ranges):
                # print(ranges[cur_range])
                if ranges[cur_range][0] > t:
                    return False
                if ranges[cur_range][1] < t:
                    cur_range += 1
                else:
                    found = True
                    break
            if not found:
                return False
        
        return True