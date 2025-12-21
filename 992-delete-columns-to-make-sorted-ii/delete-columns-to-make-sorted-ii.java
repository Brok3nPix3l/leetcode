class Solution {
    public int minDeletionSize(String[] strs) {
        final int n = strs.length;
        final int m = strs[0].length();
        int ans = 0;
        List<Integer> stringsThatAreSortedAddedFromThisColumn = new ArrayList<>();
        Set<Integer> stringsThatAreSorted = new HashSet<>();
        Set<Integer> removedColumns = new HashSet<>();
        for (int column = 0; column < m; column++) {
            if (removedColumns.contains(column)) {
                continue;
            }
            for (int string = 0; string < n - 1; string++) {
                if (stringsThatAreSorted.contains(string)) {
                    continue;
                }
                char[] currentStr = strs[string].toCharArray();
                char[] nextStr = strs[string + 1].toCharArray();
                if (nextStr[column] < currentStr[column]) {
                    // we must remove this column
                    ans++;
                    // other strings that we columnust determined are sorted might not actually be because we are removing this column
                    stringsThatAreSortedAddedFromThisColumn.clear();
                    removedColumns.add(column);
                    // System.out.println("removing column " + column);
                    break;
                }
                if (nextStr[column] > currentStr[column]) {
                    // currentString is already sorted
                    stringsThatAreSortedAddedFromThisColumn.add(string);
                    continue;
                }
                // if they are equal, continue evaluating
            }
            // if we've made it through the entire column without removing it, add actually add all of the newly sorted strings to the set
            stringsThatAreSorted.addAll(stringsThatAreSortedAddedFromThisColumn);
        }
        return ans;
    }
}