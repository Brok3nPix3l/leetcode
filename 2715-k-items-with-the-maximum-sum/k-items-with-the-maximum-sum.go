func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
    // if numOnes >= k, return k
    if (numOnes >= k) {
        return k
    }
    // k -= numOnes
    k -= numOnes
    fmt.Println(k)
    // if numZeros >= k, return numOnes
    if (numZeros >= k) {
        return numOnes
    }
    // k -= numZeros
    k -= numZeros
    fmt.Println(k)
    // if k >= numNegOnes, return numOnes - numNegOnes
    if (k >= numNegOnes) {
        return numOnes - numNegOnes
    }
    // return numOnes - k
    return numOnes - k
}