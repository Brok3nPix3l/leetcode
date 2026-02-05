class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = [[i, count] for i, count in enumerate(tickets)]
        # print(queue)
        
        time = 0
        while queue:
            time += 1
            cur = queue.pop(0)
            # print(f'time={time} cur={cur} queue={queue} ')
            if cur[1] == 1:
                if cur[0] == k:
                    return time
                continue
            cur[1] -= 1
            queue.append(cur)
        
        return -1