class Solution {
    public int countPartitions(int[] nums) {
        int rightSum = 0;
        for (int i = 0; i < nums.length; i++) {
            rightSum += nums[i];
        }
        int leftSum = 0;
        int ans = 0;
        for (int i = nums.length - 1; i > 0; i--) {
            // System.out.println(Arrays.toString(Arrays.copyOfRange(nums, 0, i)) + "|" + Arrays.toString(Arrays.copyOfRange(nums, i, nums.length - 1)));
            rightSum -= nums[i];
            leftSum += nums[i];
            // System.out.println("leftSum=" + leftSum + " rightSum=" + rightSum);
            if (Math.abs(leftSum - rightSum) % 2 == 0) {
                ans++;
                // System.out.println("ans=" + ans);
            }
        }
        return ans;
    }
}