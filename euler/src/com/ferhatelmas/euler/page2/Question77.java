package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.Arrays;

public class Question77 {

    public static void main(String[] args) {

        ArrayList<Integer> primes = new ArrayList<Integer>();
        boolean[] primeFlags = new boolean[100];
        Arrays.fill(primeFlags, true);

        for(int i=2; i<primeFlags.length; i++) {
            if(primeFlags[i]) {
                primes.add(i);
                for(int j=2*i; j<primeFlags.length; j+=i) {
                    primeFlags[j] = false;
                }
            }
        }

        int upperBound = 2;
        while(true) {
            int[] cache = new int[upperBound+1];
            cache[0] = 1;

            for(int p : primes) {
                for(int j=p; j<=upperBound; j++) {
                    cache[j] += cache[j - p];
                }
            }

            if(cache[upperBound++] > 5000) break;
        }
        System.out.println(upperBound-1);
    }

}
