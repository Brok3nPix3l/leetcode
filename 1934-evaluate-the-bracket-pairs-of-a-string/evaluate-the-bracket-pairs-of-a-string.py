class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = listToDict(knowledge)
        
        ans_list = []
        l = 0
        between_parentheses = False
        for i, c in enumerate(s):
            if c == '(':
                l = i
                between_parentheses = True
            elif c == ')':
                # feather both ends inward by 1 to trim off the parentheses
                key = s[l + 1:i]
                value = knowledge_dict.get(key, '?')
                # print(f'key={key} value={value}')
                ans_list.append(value)
                between_parentheses = False
            elif not between_parentheses:
                ans_list.append(c)
        
        return ''.join(ans_list)

def listToDict(l: list[list[str]]) -> dict[str, str]:
    return {key: value for key, value in l}