class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # record all binary codes in s into a set as ints
        # iterate through all values of k and check if they were found
        codes = set()
        l = 0
        for r in range(k - 1, len(s)):
            str_code = s[l:r+1]
            int_code = int(str_code, 2) 
            # print(f'str_code={str_code} int_code={int_code}')
            codes.add(int_code)
            # if len(codes) == 2 ** k:
                # return True
            l += 1
        # return False
        # print(2 ** k - 1)
        # print(len(codes))
        return len(codes) == 2 ** k