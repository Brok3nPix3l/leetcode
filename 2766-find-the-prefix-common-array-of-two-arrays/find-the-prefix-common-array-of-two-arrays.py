class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa = set()
        sb = set()
        C = []
        for a, b in zip(A, B):
            sa.add(a)
            sb.add(b)
            C.append(len(sa & sb))

        return C