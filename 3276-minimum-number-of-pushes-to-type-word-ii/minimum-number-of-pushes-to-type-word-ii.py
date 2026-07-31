from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        the first 8 most common letters in `word` will each take 1 press
        the second 8 most common letters in `word` will each take 2 presses
        the third 8 most common letters in `word` will each take 3 presses
        the final 2 least common letters in `word` will each take 4 presses
        """
        c = Counter(word)
        mapped_letters = 0
        pushes = 0
        for letter, count in c.most_common():
            # print(letter, count)
            if mapped_letters < 8:
                # print('one push required')
                pushes += count
            elif mapped_letters < 16:
                # print('two pushes required')
                pushes += count * 2
            elif mapped_letters < 24:
                # print('three pushes required')
                pushes += count * 3
            else:
                # print('four pushes required')
                pushes += count * 4
            mapped_letters += 1
        return pushes