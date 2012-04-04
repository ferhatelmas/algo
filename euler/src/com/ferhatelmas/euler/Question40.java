package com.ferhatelmas.euler;

public class Question40 {

    public static void main(String[] args) {

        StringBuilder sb = new StringBuilder();
        
        int i=1;
        while(sb.length() < 1000000) {
            
            sb.append(i);
            i++;
            
        }
        
        int mul = 1;
        
        String s = sb.toString();
        mul *= sb.charAt(0)-'0';
        mul *= sb.charAt(9)-'0';
        mul *= sb.charAt(99)-'0';
        mul *= sb.charAt(999)-'0';
        mul *= sb.charAt(9999)-'0';
        mul *= sb.charAt(99999)-'0';
        mul *= sb.charAt(999999)-'0';

        System.out.println(mul);

    }

}
