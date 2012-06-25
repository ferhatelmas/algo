package com.ferhatelmas.euler.page2;

public class Question64 {

    public static void main(String[] args) {

        int cnt = 0;
        for(int i=2; i<=10000; i++) {
            if(getPeriod(i)) cnt++;
        }
        System.out.println(cnt);
    }

    private static boolean getPeriod(int n) {
        int m = 0, d = 1, a = (int)Math.sqrt(n), s = a;
        if(a*a == n) return false;

        int cnt = 0;
        while(a != 2*s) {
            cnt++;
            m = d*a - m;
            d = (n - m*m) / d;
            a = (s + m) / d;
        }

        return cnt%2 == 1;
    }

}
