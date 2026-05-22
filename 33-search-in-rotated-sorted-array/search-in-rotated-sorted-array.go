func search(nums []int, target int) int {
    // modified binary search
    // if l > r, the pivot is somewhere between

    l, r := 0, len(nums) - 1
    for l < r - 1 {
        m := (r - l) / 2 + l
        // fmt.Println("l:", l, "m:", m, "r:", r)
        if target == nums[m] {
            return m
        } else if target > nums[m] && target > nums[len(nums) - 1] && nums[m] < nums[len(nums) - 1] {
            r = m - 1
        } else if target > nums[m] {
            l = m + 1
        } else if target < nums[m] && target < nums[0] && nums[m] > nums[0] {
            l = m + 1
        } else if target < nums[m] {
            r = m - 1
        }
    }

    if l >= 0 && l < len(nums) && nums[l] == target {
        return l
    } else if r >= 0 && r < len(nums) && nums[r] == target {
        return r
    } else {
        return -1
    }
}