func numberOfSpecialChars(word string) int {
    var seen [58]bool
    for _, c := range word {
        seen[c - 'A'] = true
    }
    specialChars := 0
    for i := 0; i < 26; i++ {
        if seen[i] && seen[i + 32] {
            specialChars += 1
        }
    }
    return specialChars
}