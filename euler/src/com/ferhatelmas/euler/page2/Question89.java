package com.ferhatelmas.euler.page2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Question89 {

    private static char[] chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    private static int[] values = {1, 5, 10, 50, 100, 500, 1000};
    private static String[] str = {"IIII", "XXXX", "CCCC", "VIV", "LXL", "DCD"};
    private static String[] rep = {"IV", "XL", "CD", "IX", "XC", "CM"};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("roman.txt"));

        int sum = 0;

        String line;
        while((line=br.readLine()) != null) {
            sum += getProfit(line);
        }
        System.out.println(sum);
    }

    private static int getProfit(String s) {
        String sn = getConversion(getRoman(getNumber(s), values.length-1));
        return s.length()-sn.length();
    }

    private static String getConversion(String s) {
        for(int i=0; i<str.length; i++) {
            s = s.replaceAll(str[i], rep[i]);
        }
        return s;
    }

    private static String getRoman(int n, int offset) {

        StringBuilder sb = new StringBuilder();
        for(int i=offset; i>-1; i--) {

            while(n >= values[i]) {
                sb.append(chars[i]);
                n -= values[i];
            }
        }
        return sb.toString();
    }

    private static int getNumber(String s) {

        int sum = 0, len = s.length();
        for(int i=0; i<len; i++) {
            if(i != len-1) {
                int curr = getVal(s.charAt(i));
                int next = getVal(s.charAt(i+1));
                if(next > curr) sum -= curr;
                else sum += curr;
            } else {
                sum += getVal(s.charAt(i));
            }
        }
        return sum;
    }

    private static int getVal(char c) {
        for(int i=0; i<chars.length; i++) {
            if(c == chars[i]) return values[i];
        }
        return -1;
    }
}
