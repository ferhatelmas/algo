package com.ferhatelmas.euler.page4;

import java.util.Arrays;

public class Question179 {

    public static void main(String[] args) {
        
        int[] cache = new int[10000001];
        int p;

        Arrays.fill(cache, 2); // 1 and number itself

        for(int i=2; i<= Math.sqrt(cache.length-1); i++) {
            p = i*i;    // exact square brings 1 divisor
            cache[p]--; // we will add two, so substract 1
            while(p < cache.length) {
                cache[p] += 2;
                p += i;
            }
        }

        int cnt = 0;
        for(int i=2; i<cache.length-1; i++) {
            if(cache[i] == cache[i+1]) cnt++;
        }
        System.out.println(cnt);
    }

}
