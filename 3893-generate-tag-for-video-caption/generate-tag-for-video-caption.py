class Solution:
    def generateTag(self, caption: str) -> str:
        words = [word for word in caption.split(' ') if len(word) > 0]
        if len(words) == 0:
            return '#'

        return f'#{words[0].lower()}{"".join(map(titleCase, words[1:]))}'[:100]

def titleCase(word: str) -> str:
    return f'{word[0].upper()}{word[1:].lower()}'