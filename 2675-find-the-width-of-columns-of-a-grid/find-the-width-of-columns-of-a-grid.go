func findColumnWidth(grid [][]int) []int {
    widths := []int{}
    for _, nums := range grid {
        for j, num := range nums {
            // fmt.Println("j:", j, "num:", num)
            if j >= len(widths) {
                widths = append(widths, intLen(num))
            } else {
                widths[j] = max(widths[j], intLen(num))
            }
        }
    }
    return widths
}

func intLen(i int) int {
    if i == 0 {
        return 1
    }
    length := 0
    if i < 0 {
        length = 1
        i = -i
    }
    switch {
        case i < 10:
            return length + 1
        case i < 100:
            return length + 2
        case i < 1000:
            return length + 3
        case i < 10000:
            return length + 4
        case i < 100000:
            return length + 5
        case i < 100000:
            return length + 5
        case i < 1000000:
            return length + 6
        case i < 10000000:
            return length + 7
        case i < 100000000:
            return length + 8
        case i < 1000000000:
            return length + 9
        default:
            return length + 10
    }
}