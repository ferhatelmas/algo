package com.ferhatelmas.euler.page6;

import java.util.ArrayList;

public class Question297 {

    public static void main(String[] args) {

        long limit = (long)Math.pow(10, 17);

        ArrayList<Long> cacheFib = new ArrayList<Long>();
        ArrayList<Long> cacheZ = new ArrayList<Long>();
        cacheFib.add(0L); cacheFib.add(1L); cacheFib.add(2L);
        cacheZ.add(0L); cacheZ.add(0L); cacheZ.add(1L);
        long n = 3, prev = 2;

        int i = 2;
        while(n < limit) {
            cacheFib.add(n);
            cacheZ.add(cacheZ.get(i) + cacheZ.get(i-1) + cacheFib.get(i-1));
            long l = n;
            n += prev;
            prev = l;
            i++;
        }

        System.out.println(getZ(cacheFib, cacheZ, limit));

    }

    public static long getZ(ArrayList<Long> cacheFib, ArrayList<Long> cacheZ, long n) {

        if(n < 3) {
            return cacheZ.get((int)n);
        }

        int i = cacheFib.size()-1;
        while(cacheFib.get(i) > n) i--;

        return cacheZ.get(i) + getZ(cacheFib, cacheZ, n-cacheFib.get(i)) + n - cacheFib.get(i);
    }

}