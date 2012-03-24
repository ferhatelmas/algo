package com.ferhatelmas;

import java.math.BigInteger;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/15/12
 * Time: 6:23 AM
 * To change this template use File | Settings | File Templates.
 */
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
