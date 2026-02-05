class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(word) for word in s.split(" ") if word.isdigit()]
        # print(numbers)
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i+1]:
                return False
        
        return True