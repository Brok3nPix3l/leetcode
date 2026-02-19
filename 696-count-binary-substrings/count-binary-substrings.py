class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = [0, 0]
        cur = s[0]
        ans = 0
        for i in s:
            if i != cur:
                if counts[0] and counts[1]:
                    ans += min(counts[0], counts[1])
                cur = i
                counts[int(cur)] = 1
            else:
                counts[int(i)] += 1
            # print(counts)
        ans += min(counts[0], counts[1])
        return ans