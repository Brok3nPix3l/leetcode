class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer,Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        int sum = 0;
        for (Map.Entry<Integer,Integer> e : freqMap.entrySet()) {
            if (e.getValue() != 1) {
                continue;
            }
            sum += e.getKey();
        }
        return sum;
    }
}