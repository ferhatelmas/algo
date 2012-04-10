package com.ferhatelmas.euler.page1;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Question41 {

    static Pattern pattern1 = Pattern.compile(".*(\\d).*\\1.*");
    static Pattern pattern2 = Pattern.compile(".*0.*");

    public static void main(String[] args) {
        
        for(int i=98765430; i>0; i--) {
            
            if(isPanDigital(i) && isPrime(i)) {

                System.out.println(i);
                break;
                
            }
            
        }
        
    }

    private static boolean isPrime(int num) {

        if(num < 2) return false;

        if(num%2 == 0) return false;

        for(int i=2; i<=Math.sqrt(num); i++) {

            if(num%i == 0) return false;

        }

        return true;

    }

    private static boolean isPanDigital(int num) {

        String s = String.valueOf(num);
        int n = s.length();
        
        if(n < 9) {
            
            for(int i=0; i<n; i++) {
                
                if(s.charAt(i)-'0' > n) return false;
                
            }
            
        }
        
        Matcher matcher1 = pattern1.matcher(s);
        Matcher matcher2 = pattern2.matcher(s);

        return !(matcher1.matches() || matcher2.matches());
    }
    
}
