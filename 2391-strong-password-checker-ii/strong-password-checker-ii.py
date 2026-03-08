class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        contains_lowercase_letter = False
        for c in password:
            if c.islower():
                contains_lowercase_letter = True
                break
        if not contains_lowercase_letter:
            return False
        contains_uppercase_letter = False
        for c in password:
            if c.isupper():
                contains_uppercase_letter = True
                break
        if not contains_uppercase_letter:
            return False
        contains_digit = False
        for c in password:
            if c.isdigit():
                contains_digit = True
                break
        if not contains_digit:
            return False
        contains_special_character = False
        for c in password:
            if c in "!@#$%^&*()-+":
                contains_special_character = True
                break
        if not contains_special_character:
            return False
        for i, c in enumerate(password[:-1]):
            if password[i+1] == c:
                return False
        return True