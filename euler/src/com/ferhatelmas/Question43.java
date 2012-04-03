package com.ferhatelmas;

import java.math.BigInteger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Question43 {

    static Pattern pattern1 = Pattern.compile(".*(\\d).*\\1.*");

    public static void main(String[] args) {

        BigInteger sum = new BigInteger("0");
        
        BigInteger i = new BigInteger("1000000000");
        BigInteger max = new BigInteger("10000000000");
        
        for(; i.compareTo(max) < 0;) {

            if(isPanDigital(i) && isDivisible(i)) sum = sum.add(i);

            i = i.add(new BigInteger("1"));
        }

        System.out.println(sum);

    }
    
    private static boolean isDivisible(BigInteger i) {
        
        String s = i.toString();

        if(Integer.parseInt(s.substring(1, 4))%2 == 0 &&
           Integer.parseInt(s.substring(2, 5))%3 == 0 &&
           Integer.parseInt(s.substring(3, 6))%5 == 0 &&
           Integer.parseInt(s.substring(4, 7))%7 == 0 &&
           Integer.parseInt(s.substring(5, 8))%11 == 0 &&
           Integer.parseInt(s.substring(6, 9))%13 == 0 &&
           Integer.parseInt(s.substring(7))%17 == 0) return true;

        return false;
        
    }

    private static boolean isPanDigital(BigInteger num) {

        String s = num.toString();

        Matcher matcher1 = pattern1.matcher(s);

        return !matcher1.matches();
    }

}
