class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        Map<Integer,Integer> digitalSumFreqMap = new HashMap<>();
        int maxFreq = 0;
        int curDigitalSum = computeDigitalSum(lowLimit);
        for (int i = lowLimit; i <= highLimit; i++) {
            digitalSumFreqMap.put(curDigitalSum, digitalSumFreqMap.getOrDefault(curDigitalSum, 0) + 1);
            maxFreq = Math.max(digitalSumFreqMap.get(curDigitalSum), maxFreq);
            
            int temp = i;
            while (temp >= 9 && temp % 10 == 9) {
                curDigitalSum -= 9;
                temp /= 10;
            }
            curDigitalSum++;
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