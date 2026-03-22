class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rc = Counter(ranks)
        sc = Counter(suits)
        if sc.most_common(1)[0][1] >= 5:
            return 'Flush'
        if rc.most_common(1)[0][1] >= 3:
            return 'Three of a Kind'
        if rc.most_common(1)[0][1] >= 2:
            return 'Pair'
        return 'High Card'