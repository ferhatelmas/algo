package com.ferhatelmas;

import java.math.BigInteger;

public class Question55 {

    private static BigInteger one = new BigInteger("1");
    
    public static void main(String[] args) {

        BigInteger b = new BigInteger("1");
        int cnt = 0;
        
        for(int i=1; i<10000; i++) {

            if(isLychrel(b)) cnt++;

            b = b.add(one);
        }

        System.out.println(cnt);
        
    }
    
    private static boolean isLychrel(BigInteger b) {
        
        for(int i=0; i<50; i++) {
            
            BigInteger br = new BigInteger(new StringBuilder(b.toString()).reverse().toString());
            
            b = b.add(br);
            
            if(isPalindrome(b.toString())) return false;
            
        }
        
        return true;
        
    }
    
    private static boolean isPalindrome(String s) {
        
        for(int i=0; i<s.length()/2; i++) {
            
            if(s.charAt(i) != s.charAt(s.length()-i-1)) return false;
            
        }

        return true;
        
    }
    
}
