class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c1 = Counter(c for c in s1[::2])
        c2 = Counter(c for c in s2[::2])
        c3 = Counter(c for c in s1[1::2]) 
        c4 = Counter(c for c in s2[1::2])
        # print(f'c1={c1} c2={c2} c3={c3} c4={c4}')
        return c1 == c2 and c3 == c4