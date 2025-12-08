class Solution {
    public int countTriples(int n) {
        int tripleCount = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int aAndB = a * a + b * b;
                for (int c = 1; c <= n; c++) {
                    int cSquared = c * c;
                    if (aAndB < cSquared) {
                        continue;
                    }
                    if (aAndB == cSquared) {
                        tripleCount++;
                    }
                }
            }
        }
        return tripleCount;
    }
}