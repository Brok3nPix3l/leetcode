class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        Map<Integer,Integer> digitalSumFreqMap = new HashMap<>();
        int maxFreq = 0;
        for (int i = lowLimit; i <= highLimit; i++) {
            int digitalSum = computeDigitalSum(i);
            digitalSumFreqMap.put(digitalSum, digitalSumFreqMap.getOrDefault(digitalSum, 0) + 1);
            maxFreq = Math.max(digitalSumFreqMap.get(digitalSum), maxFreq);
        }
        return maxFreq;
    }

    private int computeDigitalSum(int num) {
        int digitalSum = 0;
        for (char c : String.valueOf(num).toCharArray()) {
            digitalSum += c - '0';
        }
        return digitalSum;
    }
}