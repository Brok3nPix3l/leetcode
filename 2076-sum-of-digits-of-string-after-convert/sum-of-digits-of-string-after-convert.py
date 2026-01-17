class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = "".join([str(ord(c) - ord('a') + 1) for c in s])
        for n in range(k):
            converted = str(sum(int(d) for d in converted))
        return int(converted)