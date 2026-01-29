import string

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost_letter_convert_dict = self.generate_min_cost_letter_convert_dict(original, changed, cost)
        # filtered_min_cost_letter_convert_dict = {s: {t: c for t, c in target_cost.items() if c != float('inf') and s != t} for s, target_cost in min_cost_letter_convert_dict.items()}
        # for s, tc in list(filtered_min_cost_letter_convert_dict.items()):
        #     if len(tc) == 0:
        #         del filtered_min_cost_letter_convert_dict[s]
        # print(f'min_cost_letter_convert_dict = {filtered_min_cost_letter_convert_dict}')
        total_cost = 0
        for i, (s, t) in enumerate(zip(source, target)):
            # print(f"i={i}: {s} -> {t}")
            if t == s:
                continue
            change_cost = min_cost_letter_convert_dict[s][t]
            if change_cost == float("inf"):
                return -1
            total_cost += change_cost

        return total_cost

    def generate_min_cost_letter_convert_dict(self, original: List[str], changed: List[str], cost: List[int]) -> dict[chr, dict[chr, int | float("inf")]]:
        # 26 * 26 dict for converting each letter from 'a' to 'z' to each other letter from 'a' to 'z'
        # initially, all paths are impossible
        dist = {s: {t: (0 if t == s else float("inf")) for t in string.ascii_lowercase} for s in string.ascii_lowercase}

        # initialize the provided edges
        for o, c, z in zip(original, changed, cost):
            dist[o][c] = min(dist[o][c], z)

        # source -> target = minimum of:
        # - source -> target
        # - source -> intermediary -> target
        for i in string.ascii_lowercase:
            for s in string.ascii_lowercase:
                if dist[s][i] == float('inf'):
                    continue
                for t in string.ascii_lowercase:
                    if dist[i][t] == float('inf'):
                        continue
                    dist[s][t] = min(dist[s][t], dist[s][i] + dist[i][t])
        
        return dist