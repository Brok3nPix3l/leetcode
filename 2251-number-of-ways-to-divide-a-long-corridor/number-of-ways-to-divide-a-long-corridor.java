// remove leading and trailing Ps
// remove contiguous sections of the pattern SP+S
// map each remaining section of Ps to its length + 1
// reduce to the product of the values
// if there are an odd number of S's (or 0), return 0 instead

// "SSPPSPS"
// SS PP SPS
// PP
// 2+1 = 3 -> 3

// "PPSPSP"
// PP SPS P
// ""
// 0+1 = 1 -> 1

// "S"
// only 1 S -> 0

// "SSPSSPSSSPPSPSPPS"
// SS P SS P SS SPPS P SPPS
// P P P
// 2*2*2 = 8 -> 8

// "SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"
// SPPPPPPPS PPP SPS SS PPPPPPPPPPPPPPPPP SPPPPPPPPPPPPPPPPS PPPPP SPS PPPPPP SPS PP SPS PPP SPS PP SS PPPPP SPPS SPP
// PPP PPPPPPPPPPPPPPPPP PPPPP PPPPPP PP PPP PP PPPPP SPP
// odd number of S's -> 0
// "PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"
// PPPPP SPPS PP SPPPS PPPP SPPPPS PPPP SPPS PPP SPS PPP SPS PPP SPS PPP SPS PPPP SPPPPS PPP SPPS PPPP SPS PPPP SPS PPPP SPS PPP SPPS PPPP SPS P SS
// PP   PPPP    PPPP    PPP PPP PPP PPP PPPP    PPP PPPP    PPPP    PPPP    PPP PPPP    P
// 2+1 *4+1 *   4+1*    3+1*3+1*3+1*3+1*4+1*    3+1*4+1*    4+1*    4+1*    3+1*4+1*    1+1
// 3 *  5 *     5 *     4 * 4 * 4 * 4 * 5 *     4 * 5 *     5 *     5 *     4 * 5 *     2
// actual: 1,920,000,000
// expected: 919,999,993

class Solution {
    private static final char SEAT = 'S';
    private static final char PLANT = 'P';
    private static final int MOD = 1000000007;

    public int numberOfWays(String corridor) {
        int ans = 0;
        int seats = 0;
        int plants = 0;
        // StringBuilder sb = new StringBuilder();
        for (int i = 0; i < corridor.length(); i++) {
            switch (corridor.charAt(i)) {
                case SEAT:
                    if (seats > 0 && seats % 2 == 0) {
                        ans = (int)((long)ans * (plants + 1) % MOD);
                        plants = 0;
                        // sb.append(" ");
                    }
                    seats++;
                    if (seats == 2 && ans == 0) {
                        ans = 1;
                    }
                    break;
                case PLANT:
                    if (seats < 2 || seats % 2 == 1) {
                        continue;
                    }
                    // sb.append(PLANT);
                    plants++;
                    break;
            }
        }
        // System.out.println(sb.toString());
        return seats % 2 == 0 ? ans : 0;
    }
}