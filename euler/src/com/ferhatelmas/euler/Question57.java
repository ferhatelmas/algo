package com.ferhatelmas.euler;

import java.math.BigInteger;

public class Question57 {

    public static void main(String[] args) {

        BigInteger num = new BigInteger("7");
        BigInteger den = new BigInteger("5");
        int cnt = 0;

        for(int i=2; i<1001; i++) {

            num = num.add(den);

            BigInteger tmp = num;
            num = den;
            den = tmp;

            num = num.add(den);

            if(num.toString().length() > den.toString().length()) {

                cnt++;
            }

        }

        System.out.println(cnt);

    }



}
