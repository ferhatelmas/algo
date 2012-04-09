package com.ferhatelmas.euler.page2;

import java.math.BigInteger;

public class Question97 {

    public static void main(String[] args) {

        BigInteger b = new BigInteger("2");
        b = b.pow(7830457).multiply(new BigInteger("28433")).add(new BigInteger("1"));
        
        String s = b.toString();

        System.out.println(s.substring(s.length()-10));

    }

}
