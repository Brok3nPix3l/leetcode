class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        set1 = Counter()
        set1[s1[0]] += 1
        set1[s1[2]] += 1
        set2 = Counter()
        set2[s2[0]] += 1
        set2[s2[2]] += 1
        if set1 - set2 or set2 - set1:
            return False
        
        set3 = Counter()
        set3[s1[1]] += 1
        set3[s1[3]] += 1
        set4 = Counter()
        set4[s2[1]] += 1
        set4[s2[3]] += 1
        if set3 - set4 or set4 - set3:
            return False

        return True