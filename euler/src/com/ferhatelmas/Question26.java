package com.ferhatelmas;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/1/12
 * Time: 1:34 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question26 {

    public static void main(String[] args) {

        int max = 0, curr = 0;

        BigDecimal one = new BigDecimal("1.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");
        MathContext mc = new MathContext(20000);

        for(int i=1; i<1000; i++) {

            BigDecimal b = one.divide(new BigDecimal(String.valueOf(i)), mc);
            
            String s = b.toString().substring(2);
            s = findSequence1(s);
            s = findSequence2(s);
            if(s == null) continue;
            
            int cnt = s.length();

            if(cnt > max) {

                max = cnt;
                curr = i;

            }

            System.out.println(i + " " + b.toString() + " " + s + " " + cnt);

        }

        System.out.println(curr);

    }

    private static String findSequence1(String text) {
        Pattern pattern = Pattern.compile(".*?(.*)\\1+.*?");
        Matcher matcher = pattern.matcher(text);
        return matcher.matches() ? matcher.group(1) : null;
    }

    private static String findSequence2(String text) {
        Pattern pattern = Pattern.compile("(.+?)\\1+");
        Matcher matcher = pattern.matcher(text);
        return matcher.matches() ? matcher.group(1) : null;
    }

}
