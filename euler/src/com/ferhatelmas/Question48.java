package com.ferhatelmas;

import java.math.BigInteger;

public class Question48 {

    public static void main(String[] args) {

        BigInteger b = new BigInteger("1");
        BigInteger sum = new BigInteger("0");
        
        for(int i=1; i<=1000; i++) {
            
            sum = sum.add(b.pow(i));
            b = b.add(new BigInteger("1"));
            
        }

        String s = sum.toString();
        System.out.println(s.substring(s.length()-10));
        
    }
    
}
