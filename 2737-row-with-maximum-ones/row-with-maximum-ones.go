func rowAndMaximumOnes(mat [][]int) []int {
    maxOnesRowIdx, maxOnesCount := 0, 0
    for i, row := range mat {
        curCount := 0
        for _, cell := range row {
            if cell == 1 {
                curCount += 1
            }
        }
        if curCount > maxOnesCount {
            maxOnesRowIdx = i
            maxOnesCount = curCount
        }
    }
    return []int{maxOnesRowIdx, maxOnesCount}
}