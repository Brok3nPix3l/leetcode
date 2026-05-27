class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars_map = {}
        for i, c in enumerate(word):
            if c.lower() not in chars_map:
                chars_map[c.lower()] = {}
            if c == c.lower():
                chars_map[c.lower()]['last_lower'] = i
            elif 'first_upper' not in chars_map[c.lower()]:
                chars_map[c.lower()]['first_upper'] = i
        ans = 0
        for c, cm in chars_map.items():
            if 'last_lower' in cm and 'first_upper' in cm and cm['last_lower'] < cm['first_upper']:
                ans += 1
        return ans