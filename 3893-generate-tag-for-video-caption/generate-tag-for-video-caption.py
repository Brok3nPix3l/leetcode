class Solution:
    def generateTag(self, caption: str) -> str:
        words = [word for word in caption.split(' ') if len(word) > 0]
        if len(words) == 0:
            return '#'

        return f'#{words[0].lower()}{"".join(word.capitalize() for word in words[1:])}'[:100]