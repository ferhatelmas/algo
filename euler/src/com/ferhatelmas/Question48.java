package com.ferhatelmas;

import java.math.BigInteger;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/8/12
 * Time: 6:54 AM
 * To change this template use File | Settings | File Templates.
 */
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
