package com.ferhatelmas.euler.page2;

import java.util.HashSet;

public class Question74 {

    private static int[] cache = new int[10];

    public static void main(String[] args) {
        fillCache();

        int cnt = 0;
        for(int i=0; i<1000000; i++) {
            if(getChainLength(i) == 60) cnt++;
        }
        System.out.println(cnt);
    }

    private static int getChainLength(long n) {

        HashSet<Long> set = new HashSet<Long>();
        set.add(n);
        n = getNewNumber(n);

        int cnt = 1;
        while(!set.contains(n)) {
            cnt++;
            set.add(n);
            n = getNewNumber(n);
        }
        return cnt;
    }

    private static long getNewNumber(long l) {
        long sum = 0;
        String s = String.valueOf(l);

        for(int i=0; i<s.length(); i++) {
            sum += cache[s.charAt(i)-'0'];
        }
        return sum;
    }

    private static void fillCache() {
        int fact = 1;
        cache[0] = fact;
        for(int i=1; i<10; ) {
            cache[i] = fact;
            fact *= ++i;
        }
    }


}
