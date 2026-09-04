class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        
        for command in commands:
            match command:
                case "UP": y -= 1
                case "RIGHT": x += 1
                case "DOWN": y += 1
                case "LEFT": x -= 1
        
        return y * n + x