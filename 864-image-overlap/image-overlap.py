from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def one_positions(img: List[List[int]]) -> List[Tuple[int, int]]:
            ans = []
            
            for y, row in enumerate(img):
                for x, cell in enumerate(row):
                    if cell == 1:
                        ans.append((x, y))
            
            return ans
        
        img1_one_positions = one_positions(img1)
        img2_one_positions = one_positions(img2)

        translations_1_to_2 = defaultdict(int)
        largest_overlap_count = 0
        for x1, y1 in img1_one_positions:
            for x2, y2 in img2_one_positions:
                delta = (x2 - x1, y2 - y1)
                translations_1_to_2[delta] += 1
                if translations_1_to_2[delta] > largest_overlap_count:
                    largest_overlap_count = translations_1_to_2[delta]
        
        translations_2_to_1 = defaultdict(int)
        for x1, y1 in img2_one_positions:
            for x2, y2 in img1_one_positions:
                delta = (x2 - x1, y2 - y1)
                translations_2_to_1[delta] += 1
                if translations_2_to_1[delta] > largest_overlap_count:
                    largest_overlap_count = translations_2_to_1[delta]
        
        return largest_overlap_count