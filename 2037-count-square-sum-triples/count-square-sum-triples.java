class Solution {
    public int countTriples(int n) {
        int tripleCount = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int aAndB = a * a + b * b;
                for (int c = 1; c <= n; c++) {
                    if (aAndB < c * c) {
                        continue;
                    }
                    if (aAndB == c * c) {
                        tripleCount++;
                    }
                }
            }
        }
        return tripleCount;
    }
}