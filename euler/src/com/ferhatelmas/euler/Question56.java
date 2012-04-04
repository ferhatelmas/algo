package com.ferhatelmas.euler;

import java.math.BigInteger;

public class Question56 {

    public static void main(String[] args) {

        int max = Integer.MIN_VALUE;

        for(int i=1; i<100; i++) {
            
            for(int j=1; j<100; j++) {

                BigInteger b = new BigInteger(String.valueOf(i));
                b = b.pow(j);
                
                int val = getSum(b.toString());
                
                if(val > max) max = val;
                
            }
            
        }

        System.out.println(max);
        
    }
    
    private static int getSum(String s) {
        
        int sum = 0;
        
        for(int i=0; i<s.length(); i++) {
            
            sum += s.charAt(i) - '0';
            
        }

        return sum;
        
    }
    
}
