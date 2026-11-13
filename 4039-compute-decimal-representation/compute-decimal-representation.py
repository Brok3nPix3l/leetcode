from collections import deque

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        components = deque()

        exp = 0
        while n > 0:
            if n % 10 != 0:
                components.appendleft((n % 10) * 10 ** exp)
            
            n //= 10
            exp += 1
        
        return list(components)