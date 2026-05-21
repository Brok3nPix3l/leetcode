const maxNum = 9

func minNumber(nums1 []int, nums2 []int) int {
    nums1Set := make(map[int]struct{})
    for _, v := range nums1 {
        nums1Set[v] = struct{}{}
    }
    minValInBothArrays := maxNum + 1
    for _, v := range nums2 {
        if _, ok := nums1Set[v]; ok {
            minValInBothArrays = min(v, minValInBothArrays)
        }
    }
    if minValInBothArrays <= maxNum {
        return minValInBothArrays
    }
    nums1Min := slices.Min(nums1)
    nums2Min := slices.Min(nums2)
    // fmt.Println("nums1 min val:", nums1Min, "nums2 min val:", nums2Min)
    ans, _ := strconv.Atoi(strconv.Itoa(min(nums1Min, nums2Min)) + strconv.Itoa(max(nums1Min, nums2Min)))
    return ans
}