class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        components = []
        exp = 0

        while n > 0:
            if n % 10 != 0:
                components.append((n % 10) * 10 ** exp)
            
            n //= 10
            exp += 1
        
        return list(reversed(components))