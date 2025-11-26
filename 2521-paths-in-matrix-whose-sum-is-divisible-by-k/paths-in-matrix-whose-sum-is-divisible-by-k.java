// for each cell of the grid, track the number of ways to reach it with a given modulo
// iterate from the top left to the bottom right, visiting each cell once
// when visiting a new cell with adjacent visited neighbors, offset the sums of the counts of those adjacent neighbor(s) with the remainder of the current cell modulo k
// return the number of ways to reach the final cell with a remainder of 0

class Solution {
    private static final int MOD = 1000000007;
    public int numberOfPaths(int[][] grid, int k) {
        final int n = grid.length, m = grid[0].length;
        Map<Integer, Map<Integer, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                // determine which of up and left neighbors have been visited (which means they have an entry in dp)
                // if current cell value % k != 0, then add remainder to each key in adjacent neighbors' maps and merge them into current cell's map
                int rem = grid[r][c] % k;
                Map<Integer, Integer> numWaysToApproachByRem = new HashMap<>();
                if (r == 0 && c == 0) {
                    numWaysToApproachByRem.put(rem, 1);
                }
                if (r != 0) {
                    Map<Integer, Integer> numWaysToApproachAboveNeighborByRem = dp.get(r - 1).get(c);
                    for (Map.Entry<Integer, Integer> e : numWaysToApproachAboveNeighborByRem.entrySet()) {
                        numWaysToApproachByRem.put((e.getKey() + rem) % k,
                                (numWaysToApproachByRem.getOrDefault((e.getKey() + rem) % k, 0) + e.getValue()) % MOD);
                    }
                }
                if (c != 0) {
                    Map<Integer, Integer> numWaysToApproachLeftNeighborByRem = dp.get(r).get(c - 1);
                    for (Map.Entry<Integer, Integer> e : numWaysToApproachLeftNeighborByRem.entrySet()) {
                        numWaysToApproachByRem.put((e.getKey() + rem) % k,
                                (numWaysToApproachByRem.getOrDefault((e.getKey() + rem) % k, 0) + e.getValue()) % MOD);
                    }
                }
                dp.computeIfAbsent(r, _ -> new HashMap<>()).put(c, numWaysToApproachByRem);
            }
        }
        // System.out.println(dp);
        return dp.get(n - 1).get(m - 1).getOrDefault(0, 0);
    }
}