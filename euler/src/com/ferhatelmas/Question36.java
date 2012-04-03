package com.ferhatelmas;

public class Question36 {

    public static void main(String[] args) {

        long sum = 0;
        for(int i=0; i<1000000; i++) {
            
            if(isPalindrome(String.valueOf(i)) && isPalindrome(getBase2(i))) sum += i;

        }

        System.out.println(sum);

    }
    
    private static String getBase2(int i) {
        
        StringBuilder sb = new StringBuilder();
        
        while(i>1) {
            
            sb.append(i%2);
            i /= 2;
            
        }

        sb.append(i);
        return sb.reverse().toString();
        
    }
    
    private static boolean isPalindrome(String s) {
        
        int n = s.length();
        for(int i=0; i<n/2; i++) {

            if(s.charAt(i) != s.charAt(n-i-1)) return false;

        }
        
        return true;
    }
    
}
