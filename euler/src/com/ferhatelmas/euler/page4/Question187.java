package com.ferhatelmas.euler.page4;

public class Question187 {

    private static int N = 100000000;
    private static boolean[] cache = new boolean[N+1];

    public static void main(String[] args) {

        makeCache();

        int cnt = 0;
        for(int i=4; i<N; i++) {
            if(isComposite(i)) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }

    private static boolean isComposite(int n) {

        if(cache[n]) return false;
        int cnt = 0;
        for(int i=2; i<=n; i++) {
            while (n%i == 0) {
                n /= i;
                if(++cnt > 2) return false;
            }
        }
        return cnt == 2;
    }

    private static void makeCache() {

        for (int i=2; i<cache.length; i++) {
            cache[i] = true;
        }

        for (int i=2; i*i<cache.length; i++) {
            if (cache[i]) {
                for (int j=i; i*j<cache.length; j++) {
                    cache[i*j] = false;
                }
            }
        }
    }

}
