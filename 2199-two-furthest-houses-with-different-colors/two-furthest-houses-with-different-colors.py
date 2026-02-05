class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        for i, ic in enumerate(colors):
            for j in range(i+1, len(colors)):
                jc = colors[j]
                # print(f'i={i} ic={ic} j={j} jc={jc}')
                if ic != jc:
                    max_dist = max(max_dist, abs(i - j))

        return max_dist