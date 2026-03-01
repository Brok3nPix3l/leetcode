class Solution:
    def minPartitions(self, n: str) -> int:
        # max = n[0]
        # for d in n[1:]:
        #     if d == '9':
        #         return 9
        #     if d > max:
        #         max = d
        return (max(int(d) for d in n))