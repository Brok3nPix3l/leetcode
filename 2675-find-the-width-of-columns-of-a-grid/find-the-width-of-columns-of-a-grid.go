func findColumnWidth(grid [][]int) []int {
    widths := []int{}
    for _, nums := range grid {
        for j, num := range nums {
            // fmt.Println("j:", j, "num:", num)
            curLen := len(strconv.Itoa(num))
            if j >= len(widths) {
                widths = append(widths, curLen)
            } else {
                widths[j] = max(widths[j], curLen)
            }
        }
    }
    return widths
}