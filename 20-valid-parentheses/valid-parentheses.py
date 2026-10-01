from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()

        for c in s:
            match c:
                case '(':
                    queue.append('(')
                case ')':
                    if len(queue) == 0:
                        return False
                    if queue.pop() != '(':
                        return False
                case '[':
                    queue.append('[')
                case ']':
                    if len(queue) == 0:
                        return False
                    if queue.pop() != '[':
                        return False
                case '{':
                    queue.append('{')
                case '}':
                    if len(queue) == 0:
                        return False
                    if queue.pop() != '{':
                        return False
            
        return len(queue) == 0