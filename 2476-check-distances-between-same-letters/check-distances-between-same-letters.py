class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        char_idxs = {}
        for i, c in enumerate(s):
            char_idxs.setdefault(c, []).append(i)
        for c in char_idxs:
            exp_dist = distance[ord(c) - ord('a')]
            # char_idxs[c][1] is always > char_idxs[c][0] because we iterate over `s` from i=0 to i=len(s)-1
            # so no need to abs()
            firstIdx, lastIdx = char_idxs[c]
            act_dist = lastIdx - firstIdx - 1
            if exp_dist != act_dist:
                return False
        return True