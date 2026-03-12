class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cur = ord('a')
        substitution = {' ': ' '}
        for c in key:
            if c in substitution:
                continue
            substitution[c] = chr(cur)
            cur += 1
        decoded = ''.join(substitution[c] for c in message)
        return decoded