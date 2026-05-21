const maxNum = 9

func minNumber(nums1 []int, nums2 []int) int {
    set1 := make(map[int]struct{}, len(nums1))
    for _, v := range nums1 {
        set1[v] = struct{}{}
    }
    minBoth := maxNum + 1
    for _, v := range nums2 {
        if _, ok := set1[v]; ok && v < minBoth {
            minBoth = v
        }
    }
    if minBoth <= maxNum {
        return minBoth
    }
    a, b := slices.Min(nums1), slices.Min(nums2)
    if a > b {
        a, b = b, a
    }
    ans, err := strconv.Atoi(fmt.Sprintf("%d%d", a, b))
    if err != nil {
        panic(err)
    }
    return ans
}