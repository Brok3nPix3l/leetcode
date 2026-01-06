class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        match ruleKey:
            case 'type':
                item_key_index = 0
            case 'color':
                item_key_index = 1
            case 'name':
                item_key_index = 2
        
        matching_item_count = 0
        for item in items:
            if item[item_key_index] == ruleValue:
                matching_item_count += 1
        
        return matching_item_count