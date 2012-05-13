package com.ferhatelmas.euler.page5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Question243 {

    private static double limit = 15499/94744.0;
    private static int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    public static void main(String[] args) {

        int d, base = 1;
        double p = getBasePhi(9);

        for(int i=0; i<9; i++) base *= primes[i];
        d = base;

        while(((p*d)/(d-1)) >= limit) {
            d += base;
        }
        System.out.println(d);
    }

    private static double getBasePhi(int offset) {

        double phi = 1;

        for(int i=0; i<offset; i++) {
            phi *= (primes[i]-1) / (double)primes[i];
        }

        return phi;
    }

    /* Methods for initial trials (how we got this prime range) */
    private static int getPhi(int d) {
        int cnt = 0;
        for(int i=1; i<d; i++) {
            if(gcd(d, i) == 1) cnt++;
        }
        return cnt;
    }

    private static List<Integer> getPrimes() {

        boolean[] cache = new boolean[10001];
        Arrays.fill(cache, true);

        for(int i=2; i<cache.length; i++) {
            if(!cache[i]) {
                for(int j=i; j<cache.length; j+=i) {
                    cache[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<Integer>();
        for(int i=2; i<cache.length; i++) {
            if(cache[i]) primes.add(i);
        }
        return primes;
    }

    private static int gcd(int a, int b) {

        while(b > 0) {
            a -= b;
            int tmp = Math.max(a, b);
            b = Math.min(a, b);
            a = tmp;
        }
        return a;
    }

}
