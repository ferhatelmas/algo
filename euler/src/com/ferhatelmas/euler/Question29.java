package com.ferhatelmas.euler;

import java.math.BigInteger;
import java.util.HashSet;

public class Question29 {

    private static int upperLimit = 100;
    
    public static void main(String[] args) {

        HashSet<BigInteger> set = new HashSet<BigInteger>();

        for(int i=2; i<=upperLimit; i++) {

            for(int j=2; j<=upperLimit; j++) {

                BigInteger base = new BigInteger(String.valueOf(i));
                set.add(base.pow(j));

            }

        }

        System.out.println(set.size());


    }

}
