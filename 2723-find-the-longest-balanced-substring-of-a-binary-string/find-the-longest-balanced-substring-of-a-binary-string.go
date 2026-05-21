func findTheLongestBalancedSubstring(s string) int {
    zeros, ones := 0, 0
    longest := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '1' {
            ones += 1
        } else {
            if ones > 0 {
                zeros, ones = 1, 0
            } else {
                zeros += 1
            }
        }
        longest = max(min(zeros, ones) * 2, longest)
        // fmt.Printf("[%d,%d] (%d) %d\n", i, zeros, ones, longest)
    }
    return longest
}