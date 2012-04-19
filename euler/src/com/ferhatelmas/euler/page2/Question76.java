package com.ferhatelmas.euler.page2;

import java.util.HashMap;

public class Question76 {

    private static int[] chops;

    private static HashMap<String, Integer> cache = new HashMap<String, Integer>();

    public static void main(String[] args) {
        fillChops();
        System.out.println(produce(100, 99));
    }

    private static void fillChops(){
        chops = new int[99];
        for(int i=0; i<chops.length; i++) {
            chops[i] = 99-i;
        }
    }

    private static int produce(int n, int max) {

        if(n == 0) {
            return 1;
        }
        if(n<0) return 0;

        String key = n + ":" + max;
        if(cache.containsKey(key)) return cache.get(key);

        int sum = 0;
        for(int i : chops) {
            if(i <= max) sum += produce(n-i, i);
        }
        cache.put(key, sum);
        return sum;
    }

}
