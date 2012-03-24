package com.ferhatelmas;

import java.math.BigInteger;
import java.util.HashSet;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/2/12
 * Time: 6:08 AM
 * To change this template use File | Settings | File Templates.
 */
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
