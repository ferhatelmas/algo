package com.ferhatelmas.euler;

public class Question30 {

    public static void main(String[] args) {
        
        int sum = 0;
        
        for(int i=1; i<Integer.MAX_VALUE; i++) {
            
            String s = String.valueOf(i);
            if(s.length()<2) continue;
            
            int localSum = 0;
            for(int j=0; j<s.length(); j++) {
                
                localSum += getPow(s.charAt(j)-'0');
                
            }

            if(localSum == i) {
                System.out.println(i);
                sum += i;
            } else if(Math.abs(localSum-i) > 1000000) break;
            
        }

        System.out.println(sum);
        
    }
    
    private static int getPow(int x) {
        
        int res = 1;
        
        for(int i=0; i<5; i++) {
            
            res *= x;
            
        }
        
        return res;
        
    }
    
    
}
