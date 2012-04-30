package com.ferhatelmas.euler.page2;

import java.math.BigInteger;

public class Question65 {

    public static void main(String[] args) {

        BigInteger back1 = new BigInteger("3"), back2 = new BigInteger("2");

        for(int i=2; i<100; i++) {
            BigInteger tmp = back1.multiply(new BigInteger(String.valueOf(i%3==2 ? 2*(i+1)/3 : 1))).add(back2);
            back2 = back1;
            back1 = tmp;
        }
        System.out.println(getDigitsSum(back1));
    }

    private static int getDigitsSum(BigInteger n) {
        String s = n.toString();
        int sum = 0;
        for(int i=0; i<s.length(); i++) {
            sum += s.charAt(i) - '0';
        }
        return sum;
    }

}
