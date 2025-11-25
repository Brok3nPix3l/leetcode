class Solution {
    public int maxSumDivThree(int[] nums) {
        int minModOne = Integer.MAX_VALUE, minModTwo = Integer.MAX_VALUE, secondMinModOne = Integer.MAX_VALUE, secondMinModTwo = Integer.MAX_VALUE;
        int sum = 0;
        for (int num : nums) {
            int mod = num % 3;
            if (mod == 1) {
                if (num < minModOne) {
                    secondMinModOne = minModOne;
                    minModOne = num;
                } else if (num < secondMinModOne) {
                    secondMinModOne = num;
                }
            } else if (mod == 2) {
                if (num < minModTwo) {
                    secondMinModTwo = minModTwo;
                    minModTwo = num;
                } else if (num < secondMinModTwo) {
                    secondMinModTwo = num;
                }
            }
            sum += num;
        }

        int min = Integer.MAX_VALUE;
        switch (sum % 3) {
            case 0:
                // sum is already divisible by 3, no change needed
                break;
            case 1:
                if (minModOne != Integer.MAX_VALUE) {
                    min = Math.min(min, minModOne);
                }
                if (minModTwo != Integer.MAX_VALUE && secondMinModTwo != Integer.MAX_VALUE) {   
                    min = Math.min(min, minModTwo + secondMinModTwo);
                }
                sum -= min;
                break;
            case 2:
                if (minModTwo != Integer.MAX_VALUE) {
                    min = Math.min(min, minModTwo);
                }
                if (minModOne != Integer.MAX_VALUE && secondMinModOne != Integer.MAX_VALUE) {   
                    min = Math.min(min, minModOne + secondMinModOne);
                }
                sum -= min;
                break;
        }
        return sum;
    }
}