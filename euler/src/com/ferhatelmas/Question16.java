package com.ferhatelmas;

import java.math.BigInteger;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/28/12
 * Time: 1:11 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question16 {

    public static void main(String[] args) {

        BigInteger b = new BigInteger("1");
        
        for(int i=0; i<1000; i++) {
            
            b = b.multiply(new BigInteger("2"));
            
        }
        
        String s = b.toString();
        
        int sum = 0;
        
        for(int i=0; i<s.length(); i++) {
            
            sum += s.charAt(i) - '0';
            
        }

        System.out.println(sum);
        
    }
    
}
