package com.ferhatelmas;

import java.math.BigInteger;

public class Question20 {

    public static void main(String[] args) {

        BigInteger b = new BigInteger("1");

        for(int i=2; i<101; i++) {

            b = b.multiply(new BigInteger(String.valueOf(i)));

        }

        String s = b.toString();

        int sum = 0;
        for(int i=0; i<s.length(); i++) {

            sum += s.charAt(i) - '0';

        }

        System.out.println(sum);

    }

}
