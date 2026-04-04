class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        row_length = len(encodedText) // rows
        text_by_row = [encodedText[i*row_length:i*row_length+row_length] for i in range(rows)]
        # print(text_by_row)
        r = 0
        c = 0
        original = []
        for c in range(len(text_by_row[0])):
            for r in range(rows):
                if r + c >= len(text_by_row[0]):
                    break
                original.append(text_by_row[r][c+r])
        return "".join(original).rstrip()