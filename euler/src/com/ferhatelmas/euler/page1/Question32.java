package com.ferhatelmas.euler.page1;

import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Question32 {

    static Pattern pattern1 = Pattern.compile(".*(\\d).*\\1.*");
    static Pattern pattern2 = Pattern.compile(".*0.*");

    public static void main(String[] args) {

        int mux, sum = 0;

        HashSet<Integer> set = new HashSet<Integer>();
        for(int i=100; i<10000; i++) {

            for(int j=1; j<100; j++) {

                mux = i*j;
                if(isPanDigital(i, j, mux)) {
                    System.out.println("i: " + i + " j: " + j + " mux: " + mux);
                    set.add(mux);
                }

            }

        }
        
        for(int i : set) sum += i;

        System.out.println(sum);
    }
    
    private static boolean isPanDigital(int i, int j, int mux) {
        
        StringBuilder sb = new StringBuilder();
        sb.append(i);
        sb.append(j);
        sb.append(mux);
        
        String s = sb.toString();
        if(s.length() != 9) return false;
        Matcher matcher1 = pattern1.matcher(s);
        Matcher matcher2 = pattern2.matcher(s);

        return !(matcher1.matches() || matcher2.matches());
    }

}
