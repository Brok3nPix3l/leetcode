class Solution {
    public int minOperations(String s) {
        return Math.min(startsWithZero(s), startsWithOne(s));
    }

    private int startsWithZero(String s) {
        int cur = '0';
        int diffCount = 0;
        for (char c : s.toCharArray()) {
            if (c != cur) {
                diffCount++;
            }
            cur = cur == '0' ? '1' : '0';
        }
        return diffCount;
    }
    
    private int startsWithOne(String s) {
        int cur = '1';
        int diffCount = 0;
        for (char c : s.toCharArray()) {
            if (c != cur) {
                diffCount++;
            }
            cur = cur == '0' ? '1' : '0';
        }
        return diffCount;
    }
}