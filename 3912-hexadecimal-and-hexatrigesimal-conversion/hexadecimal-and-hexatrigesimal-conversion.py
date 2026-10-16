class Solution:
    def concatHex36(self, n: int) -> str:
        return f'{base_str(16, n ** 2)}{base_str(36, n ** 3)}'

def base_str(base: int, n: int) -> str:
    # print(f'base_str base={base} n={n}')
    digits = []
    while n > 0:
        digits.append(base_chr(n % base))
        n //= base
    
    # print(digits)
    return ''.join(reversed(digits))

def base_chr(c: str) -> str:
    # print(f'base_chr c={c}')
    if c < 10:
        return str(c)
    
    return chr(ord('A') + c - 10)