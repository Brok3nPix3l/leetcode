// for each cell of the grid, track the number of ways to reach it with a given remainder mod k
// iterate from the top left to the bottom right, visiting each cell once
// when visiting a new cell, offset the sums of the counts of neighbors above and to the left with the remainder of the current cell modulo k - e.g. if the cell above can be visited two ways with a remainder of 2 mod 3 and the current cell's value is 1, then 2 + 1 = 3 mod 3 = 0, so there are now two ways to visit the current cell with a remainder of 0 mod 3
// return the number of ways to reach the final cell with a remainder of 0

class Solution {
    private static final int MOD = 1000000007;
    public int numberOfPaths(int[][] grid, int k) {
        final int n = grid.length, m = grid[0].length;
        int[][][] dp = new int[n][m][k];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                int currentRem = grid[r][c] % k;
                int[] numWaysToApproachByRem = new int[k];
                // the top-left cell can be visited in one way with its current remainder (because that's where we start)
                if (r == 0 && c == 0) {
                    numWaysToApproachByRem[currentRem] = 1;
                // determine which of the above and left neighbors have been visited (only time this isn't the case is if we're along the top or left edge of the grid)
                }
                if (r != 0) {
                    int[] numWaysToApproachAboveNeighborByRem = dp[r - 1][c];
                    for (int rem = 0; rem < k; rem++) {
                        numWaysToApproachByRem[(rem + currentRem) % k] += numWaysToApproachAboveNeighborByRem[rem];
                        // Since the answer may be very large, return it modulo 10^9 + 7.
                        numWaysToApproachByRem[(rem + currentRem) % k] %= MOD;
                    }
                }
                if (c != 0) {
                    int[] numWaysToApproachLeftNeighborByRem = dp[r][c - 1];
                    for (int rem = 0; rem < k; rem++) {
                        numWaysToApproachByRem[(rem + currentRem) % k] += numWaysToApproachLeftNeighborByRem[rem];
                        // Since the answer may be very large, return it modulo 10^9 + 7.
                        numWaysToApproachByRem[(rem + currentRem) % k] %= MOD;
                    }
                }
                dp[r][c] = numWaysToApproachByRem;
            }
        }
        // System.out.println(Arrays.deepToString(dp));
        return dp[n - 1][m - 1][0];
    }
}