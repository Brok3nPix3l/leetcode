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
        String[] parts = time.split(":");
        String hour = parts[0];
        String minute = parts[1];
        if (hour.charAt(0) == '?') {
            if (hour.charAt(1) == '?') {
                hour = "23";
            } else {
                int secondHourNum = hour.charAt(1) - '0';
                if (secondHourNum <= 3) {
                    hour = "2" + hour.charAt(1);
                } else {
                    hour = "1" + hour.charAt(1);
                }
            }
        } else {
            int firstHourNum = hour.charAt(0) - '0';
            if (hour.charAt(1) == '?') {
                if (firstHourNum == 2) {
                    hour = firstHourNum + "3";
                } else {
                    hour = firstHourNum + "9";
                }
            } // else hour is already void of any hidden digits
        }
        if (minute.charAt(0) == '?') {
            if (minute.charAt(1) == '?') {
                minute = "59";
            } else {
                // int secondMinuteNum = minute.charAt(1) - '0';
                minute = "5" + minute.charAt(1);
            }
        } else {
            int firstMinuteNum = minute.charAt(0) - '0';
            if (minute.charAt(1) == '?') {
                minute = minute.charAt(0) + "9";
            } // else minute is already void of any hidden digits
        }
        return hour + ":" + minute;
    }
}