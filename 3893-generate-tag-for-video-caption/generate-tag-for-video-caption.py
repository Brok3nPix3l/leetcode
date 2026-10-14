class Solution:
    def generateTag(self, caption: str) -> str:
        words = [word for word in caption.split(' ') if len(word) > 0]
        if len(words) == 0:
            return '#'

        first_word = words[0].lower()
        other_words_list = (word.capitalize() for word in words[1:])
        return f'#{first_word}{"".join(other_words_list)}'[:100]