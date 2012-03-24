package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/8/12
 * Time: 5:10 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question45 {

    public static void main(String[] args) {

        for(int i=144; ; i++) {

            long n = i * (2 * i - 1);

            if(isPentagonal(n)) {

                System.out.println(n);
                System.exit(0);

            }

        }

    }
    
    private static boolean isPentagonal(long n) {

        double test = (Math.sqrt(24 * n + 1) + 1) / 6;

        return (int)test == test;

    }

}
