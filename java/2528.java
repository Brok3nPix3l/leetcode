// Somehow avoid actually building the effectivePower array.
// Use just the prefix sum array for the sliding window and the priority queue comparator function.

class Solution {
    public long maxPower(int[] stations, int r, int k) {
        final int n = stations.length;
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[Math.max(i - r, 0)] += stations[i];
            prefixSum[Math.min(i + r + 1, n)] -= stations[i];
        }
        long cur = 0L;
        long[] effectivePower = new long[n];
        PriorityQueue<Integer> minPowerIndexQueue = new PriorityQueue<>(Comparator
            .comparingLong(i -> effectivePower[i]));
        for (int i = 0; i < n; i++) {
            cur += prefixSum[i];
            effectivePower[i] = cur;
            minPowerIndexQueue.add(i);
        }
        System.out.println("effectivePower: " + Arrays.toString(effectivePower));
        System.out.println("minPowerIndexQueue: " + minPowerIndexQueue);
        for (int i = 0; i < k; i++) {
            int targetStation = minPowerIndexQueue.peek();
            // sliding window from (targetStation - r) -> (targetStation + r) to find min subarray
            long windowTotalEffectivePower = 0, maxTotalEffectivePower = 0, maxTargetIndex = -1;
            int l = Math.max(targetStation - r, 0), r = l;
            int windowSize = r * 2 + 1;
            for (; r < Math.min(targetStation + r, n); r++) {
                windowTotalEffectivePower += effectivePower[r];
                while (r - l > windowSize) {
                    windowTotalEffectivePower -= effectivePower[l++];
                }
                if (r - l == windowSize) {
                    if (windowTotalEffectivePower > maxTotalEffectivePower) {
                        maxTotalEffectivePower = windowTotalEffectivePower;
                        maxTargetIndex = (r - l) / 2 + l;
                    }
                }
            }
            // insert new station at index maxTargetIndex
            prefixSum[Math.max(maxTargetIndex - r, 0)] += stations[maxTargetIndex];
            prefixSum[Math.min(maxTargetIndex + r + 1, n)] -= stations[maxTargetIndex];
            minPowerIndexQueue.remove(maxTargetIndex);
            minPowerIndexQueue.add(maxTargetIndex);
        }
        return 0L;
    }
}
