package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Question70 {

    public static void main(String[] args) {
        List<Integer> cache = fillCache(1000, 7000);

        int res = -1;
        double min = Double.MAX_VALUE;

        for(int i=0; i<cache.size(); i++) {
            for(int j=i+1; j<cache.size(); j++) {
                int n = cache.get(i)*cache.get(j);
                if(n >= 10000000) continue;

                int phi = (cache.get(i)-1)*(cache.get(j)-1);

                if(isPerm(phi, n) && n/(double)phi < min) {
                    min = n/(double)phi;
                    res = n;
                }
            }
        }
        System.out.println(res);
    }

    private static boolean isPerm(int a, int b) {
        return sort(a).equals(sort(b));
    }

    private static String sort(int n) {
        char[] c = String.valueOf(n).toCharArray();
        for(int i=0; i<c.length-1; i++) {
            for(int j=i+1; j<c.length; j++) {
                if(c[i] > c[j]) {
                    char ch = c[i];
                    c[i] = c[j];
                    c[j] = ch;
                }
            }
        }
        return new String(c);
    }

    private static List<Integer> fillCache(int min, int max) {

        boolean[] cache = new boolean[max+1];

        for (int i=2; i<cache.length; i++) {
            cache[i] = true;
        }

        for (int i=2; i*i<cache.length; i++) {
            if (cache[i]) {
                for (int j = i; i*j < cache.length; j++) {
                    cache[i*j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<Integer>();
        for(int i=min; i<=max; i++) {
            if(cache[i]) primes.add(i);
        }
        return primes;
    }

}
