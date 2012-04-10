package com.ferhatelmas.euler.page8;

public class Question357 {

    private static boolean[] cache = new boolean[100000002];

    public static void main(String[] args) {
        double start = System.currentTimeMillis();
        makeCache();
        long sum = 1;
        for(int i=2; i<cache.length; i+=2) {
            if(isPrimeGen(i)) sum += i;
        }
        System.out.println(sum);
        System.out.println(System.currentTimeMillis()-start);
    }

    private static boolean isPrimeGen(int n) {
        for(int i=1; i*i <= n; i++) {
            if(n%i == 0 && !cache[i + n/i])  return false;
        }
        return true;
    }

    private static void makeCache() {

        for (int i = 2; i < cache.length; i++) {
            cache[i] = true;
        }

        for (int i = 2; i*i < cache.length; i++) {
            if (cache[i]) {
                for (int j = i; i*j < cache.length; j++) {
                    cache[i*j] = false;
                }
            }
        }
    }

}
