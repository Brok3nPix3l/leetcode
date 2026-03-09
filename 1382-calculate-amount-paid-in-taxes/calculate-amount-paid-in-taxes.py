class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax_due = 0
        for i, bracket in enumerate(brackets):
            [upper, percent] = bracket
            dollars_taxed = min(upper, income)
            if i > 0:
                dollars_taxed -= brackets[i-1][0]
            if dollars_taxed <= 0:
                break
            tax_due += dollars_taxed * (percent / 100)
        return tax_due