class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_arr = []
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                chunk_sum = sum(int(d) for d in chunk)
                new_arr.append(str(chunk_sum))
            s = "".join(new_arr)
        return s