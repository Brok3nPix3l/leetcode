class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        contains_lowercase_letter = False
        contains_uppercase_letter = False
        contains_digit = False
        contains_special_character = False
        for i, c in enumerate(password):
            if i < len(password) - 1 and password[i+1] == c:
                return False
            if c.islower():
                contains_lowercase_letter = True
            elif c.isupper():
                contains_uppercase_letter = True
            elif c.isdigit():
                contains_digit = True
            elif c in "!@#$%^&*()-+":
                contains_special_character = True
        return contains_lowercase_letter and contains_uppercase_letter and contains_digit and contains_special_character