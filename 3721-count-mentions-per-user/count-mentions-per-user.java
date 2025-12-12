class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        Comparator<List<String>> comparator = Comparator
            .<List<String>>comparingInt(e -> Integer.parseInt(e.get(1)))
            .thenComparing(e -> !e.get(0).equals("OFFLINE"));
        events.sort(comparator);
        int[] online = new int[numberOfUsers];
        int[] mentionCount = new int[numberOfUsers];
        for (List<String> event : events) {
            int timestamp = Integer.parseInt(event.get(1));
            switch(event.get(0)) {
                case "MESSAGE":
                    switch (event.get(2)) {
                        case "ALL":
                            for (int i = 0; i < numberOfUsers; i++) {
                                mentionCount[i]++;
                            }
                            break;
                        case "HERE":
                            for (int i = 0; i < numberOfUsers; i++) {
                                if (online[i] > timestamp) {
                                    continue;
                                }
                                mentionCount[i]++;
                            }
                            break;
                        default:
                            String[] mentionedUsersStringArr = event.get(2).split(" ");
                            int[] mentionedUsers = new int[mentionedUsersStringArr.length];
                            for (int i = 0; i < mentionedUsersStringArr.length; i++) {
                                mentionedUsers[i] = Integer.parseInt(mentionedUsersStringArr[i].substring(2));
                            }
                            for (int user : mentionedUsers) {
                                mentionCount[user]++;
                            }
                    }
                    break;
                case "OFFLINE":
                    int user = Integer.parseInt(event.get(2));
                    online[user] = timestamp + 60;
                    break;
                default:
                    throw new RuntimeException("Unexpected event: " + event.get(0));
            }
        }
        return mentionCount;
    }
}