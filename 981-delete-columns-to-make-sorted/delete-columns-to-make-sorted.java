class Solution {
    public int minDeletionSize(String[] strs) {
        final int n = strs[0].length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!columnIsSorted(i, strs)) {
                ans++;
            }
        }
        return ans;
    }

    private boolean columnIsSorted(int columnIndex, String[] strs) {
        if (strs.length == 0) {
            return true;
        }
        char currentChar = strs[0].charAt(columnIndex);
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].charAt(columnIndex) < currentChar) {
                return false;
            }
            currentChar = strs[i].charAt(columnIndex);
        }
        return true;
    }

}