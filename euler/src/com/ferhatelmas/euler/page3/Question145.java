package com.ferhatelmas.euler.page3;

import java.util.regex.Pattern;

public class Question145 {

    private static int N = 1000;
    private static Pattern pattern = Pattern.compile(".*(0|2|4|6|8).*");

    public static void main(String[] args) {

        int sum = 0;
        for(int i=2; i<10; i++) {
            if(i%2 == 0) sum += 20*Math.pow(30, i/2-1);
            else if(i%4 == 3) sum += 100*Math.pow(500, i/4);
        }
        System.out.println(sum);

    }

    // if you want ;)
    private static int bruteForce() {
        int cnt = 0;
        for(int i=0; i<N; i++) {
            if(isReversible(i)) cnt++;
        }
        return cnt;
    }

    private static boolean isReversible(int i) {
        if(i%10 == 0) return false;
        return !pattern.matcher(String.valueOf(Integer.parseInt(new StringBuilder(String.valueOf(i)).reverse().toString()) + i)).matches();
    }

}
