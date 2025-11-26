// for each cell of the grid, track the number of ways to reach it with a given modulo
// iterate from the top left to the bottom right, visiting each cell once
// when visiting a new cell with adjacent visited neighbors, offset the sums of the counts of those adjacent neighbor(s) with the remainder of the current cell modulo k
// return the number of ways to reach the final cell with a remainder of 0

class Solution {
    private static final int MOD = 1000000007;
    public int numberOfPaths(int[][] grid, int k) {
        final int n = grid.length, m = grid[0].length;
        int[][][] dp = new int[n][m][k];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                // determine which of up and left neighbors have been visited (which means they have an entry in dp)
                // if current cell value % k != 0, then add remainder to each key in adjacent neighbors' maps and merge them into current cell's map
                int rem = grid[r][c] % k;
                int[] numWaysToApproachByRem = new int[k];
                if (r == 0 && c == 0) {
                    numWaysToApproachByRem[rem] = 1;
                }
                if (r != 0) {
                    int[] numWaysToApproachAboveNeighborByRem = dp[r - 1][c];
                    for (int i = 0; i < k; i++) {
                        numWaysToApproachByRem[(i + rem) % k] += numWaysToApproachAboveNeighborByRem[i];
                        numWaysToApproachByRem[(i + rem) % k] %= MOD;
                    }
                }
                if (c != 0) {
                    int[] numWaysToApproachLeftNeighborByRem = dp[r][c - 1];
                    for (int i = 0; i < k; i++) {
                        numWaysToApproachByRem[(i + rem) % k] += numWaysToApproachLeftNeighborByRem[i];
                        numWaysToApproachByRem[(i + rem) % k] %= MOD;
                    }
                }
                dp[r][c] = numWaysToApproachByRem;
            }
        }
        // System.out.println(Arrays.deepToString(dp));
        return dp[n - 1][m - 1][0];
    }
}