// hour
// ??, 2? -> 23
// [0-1]? -> [0-1]9
// ?[0-3] -> 2[0-3]
// ?[4-9] -> 1[4-9]

// minute
// ?? -> 59
// ?x -> 5x
// x? -> x9

class Solution {
    public String maximumTime(String time) {
        char h1 = time.charAt(0), h2 = time.charAt(1), m1 = time.charAt(3), m2 = time.charAt(4);
        if (h1 == '?') {
            if (h2 == '?') {
                h1 = '2';
                h2 = '3';
            } else {
                int secondHourNum = h2 - '0';
                if (secondHourNum <= 3) {
                    h1 = '2';
                } else {
                    h1 = '1';
                }
            }
        } else {
            int firstHourNum = h1 - '0';
            if (h2 == '?') {
                if (firstHourNum == 2) {
                    h2 = '3';
                } else {
                    h2 = '9';
                }
            } // else hour is already void of any hidden digits
        }
        if (m1 == '?') {
            if (m2 == '?') {
                m1 = '5';
                m2 = '9';
            } else {
                // int secondMinuteNum = m2 - '0';
                m1 = '5';
            }
        } else {
            int firstMinuteNum = m1 - '0';
            if (m2 == '?') {
                m2 = '9';
            } // else minute is already void of any hidden digits
        }
        return "" + h1 + h2 + ":" + m1 + m2;
    }
}