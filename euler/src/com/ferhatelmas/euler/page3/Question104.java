package com.ferhatelmas.euler.page3;

import java.util.regex.Pattern;

public class Question104 {

    private static Pattern pattern = Pattern.compile(".*(\\d).*\\1.*");
    private static Pattern zero = Pattern.compile(".*0.*");

    public static void main(String[] args) {

        int cnt = 3;
        int n = 2, i=1;

        while(true) {
            if(isPanLow(n)) if(isPanHigh(cnt)) break;

            int tmp = (n+i)%1000000000;
            i = n;
            n = tmp;
            cnt++;
        }
        System.out.println(cnt);
    }

    private static boolean isPanLow(int n) {
        String s = String.valueOf(n);
        return  !zero.matcher(s).matches() && !pattern.matcher(s).matches();
    }

    private static boolean isPanHigh(int cnt) {
        double phi = cnt * 0.20898764024997873 - 0.3494850021680094;
        String s = String.valueOf((int)Math.pow(10, (phi - (int) phi + 8)));
        return !zero.matcher(s).matches() && !pattern.matcher(s).matches();
    }
}
