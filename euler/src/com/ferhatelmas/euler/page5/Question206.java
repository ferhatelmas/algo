package com.ferhatelmas.euler.page5;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Question206 {

    private static Pattern pattern = Pattern.compile("^1\\d2\\d3\\d4\\d5\\d6\\d7\\d8\\d9$");

    public static void main(String[] args) {
        
        long val = (int)Math.sqrt(19293949596979899L) + 1;
        while(true) {
            Matcher m = pattern.matcher(String.valueOf(val * val));
            if(m.matches()) break;
            else val -= 2;

        }
        System.out.println(val*10);
    }

}
