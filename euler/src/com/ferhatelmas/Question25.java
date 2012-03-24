package com.ferhatelmas;

import java.math.BigInteger;

/**
 * Created by IntelliJ IDEA.
 * User: Ginger
 * Date: 28.Oca.2012
 * Time: 19:47:31
 * To change this template use File | Settings | File Templates.
 */
public class Question25 {

    public static void main(String[] args) {

        long cnt = 1;
        while(true) {

            BigInteger res = fib(cnt);
            if(res.toString().length() > 999) {
                System.out.println(cnt);
                System.exit(0);
            } else {
                cnt++;
            }

        }

    }

    private static BigInteger fib(long cnt) {

        if(cnt == 1 || cnt == 2) return new BigInteger("1");

        return fib(cnt-2).add(fib(cnt-1));

    }

}
