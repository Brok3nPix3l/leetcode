func findTheLongestBalancedSubstring(s string) int {
    l := 0
    zeroes, ones := 0, 0
    longest := 0
    for r := 0; r < len(s); r++ {
        if s[r] == '1' {
            ones += 1
        } else {
            if ones > 0 {
                l = r
                zeroes, ones = 1, 0
            } else {
                zeroes += 1
            }
        }
        longest = max(min(zeroes, ones) * 2, longest)
        fmt.Printf("[%d,%d] (%d,%d) %d\n", l, r, zeroes, ones, longest)
    }
    return longest
}