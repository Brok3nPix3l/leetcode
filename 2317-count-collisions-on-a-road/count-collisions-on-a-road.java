class Solution {
    public int countCollisions(String directions) {
        char headDirection = directions.charAt(0);
        int rightCount = headDirection == 'R' ? 1 : 0;
        int collisions = 0;
        for (int i = 1; i < directions.length(); i++) {
            char direction = directions.charAt(i);
            // System.out.println("headDirection: " + prettyPrintDirection(headDirection) + " direction: " + prettyPrintDirection(direction));
            switch (direction) {
                case 'L':
                    if (headDirection == 'S') {
                        collisions++;
                        headDirection = 'S';
                    } else if (headDirection == 'R') {
                        headDirection = 'S';
                        collisions += rightCount + 1;
                        rightCount = 0;
                    }
                    break;
                case 'S':
                    if (headDirection == 'R') {
                        collisions += rightCount;
                        rightCount = 0;
                    }
                    headDirection = 'S';
                    break;
                case 'R':
                    headDirection = 'R';
                    rightCount++;
                    break;
            }
            // System.out.println("collisions=" + collisions + " headDirection: " + prettyPrintDirection(headDirection));
        }
        return collisions;
    }

    private String prettyPrintDirection(char direction) {
        switch(direction) {
            case 'L':
                return "<-";
            case 'S':
                return "|";
            case 'R':
                return "->";
            default:
                return "?";
        }
    }
}