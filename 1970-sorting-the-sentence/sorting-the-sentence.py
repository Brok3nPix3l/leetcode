class Solution:
    def sortSentence(self, s: str) -> str:
        def split_word_and_index(word_with_index: str) -> tuple[str, int]:
            for i in range(len(word_with_index) - 1, -1, -1):
                if not word_with_index[i].isdigit():
                    return ("".join(word_with_index[0:i + 1]), int("".join(word_with_index[i + 1:])))
        
        split_words = s.split(" ")
        ordered_words = [None] * len(split_words)
        for word_with_index in split_words:
            word, index = split_word_and_index(word_with_index)
            # print(f'word={word}, index={index}')
            ordered_words[index - 1] = word
        
        return " ".join(ordered_words)