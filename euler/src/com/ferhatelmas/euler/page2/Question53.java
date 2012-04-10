package com.ferhatelmas.euler.page2;

import java.math.BigInteger;

public class Question53 {

    private static BigInteger[] cache = new BigInteger[101];
    
    public static void main(String[] args) {
        
        for(int i=0; i<=100; i++) {
            
            cache[i] = fact(i);
            
        }

        int cnt = 0;
        BigInteger b = new BigInteger("1000000");
        
        for(int i=1; i<=100; i++) {

            for(int j=1; j<=i; j++) {

                if(comb(i, j).compareTo(b) == 1) cnt++;

            }

        }

        System.out.println(cnt);
    }
    
    private static BigInteger comb(int n, int r) {

        return cache[n].divide(cache[r].multiply(cache[n-r]));
        
    }

    private static BigInteger fact(int n) {

        BigInteger mul = new BigInteger("1");
        
        for(int i=1; i<=n; i++) {
            
            mul = mul.multiply(new BigInteger(String.valueOf(i)));
            
        }

        return mul;
    }
    
}
