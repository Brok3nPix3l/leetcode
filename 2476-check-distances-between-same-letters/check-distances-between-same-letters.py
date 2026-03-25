class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        char_idxs = {}
        for i, c in enumerate(s):
            char_idxs.setdefault(c, []).append(i)
        # print(char_idxs)
        for c in char_idxs:
            exp_dist = distance[ord(c) - ord('a')]
            act_dist = abs(char_idxs[c][0] - char_idxs[c][1]) - 1
            # print(f'exp_dist={exp_dist} act_dist={act_dist}')
            if exp_dist != act_dist:
                return False
        return True