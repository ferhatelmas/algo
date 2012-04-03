package com.ferhatelmas;

public class Question34 {
    
    private static int facs[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 3602880};

    public static void main(String[] args) {

        long sum = 0;
        
        for(int i=3; i<Integer.MAX_VALUE; i++) {
            
            if(isEqual(i)) sum += i;
            
        }

        System.out.println(sum);


    }
    
    private static boolean isEqual(int num) {
        
        String s = String.valueOf(num);
        
        int sum = 0;
        
        for(int i=0; i<s.length(); i++) {
            
            sum += facs[s.charAt(i)-'0'];
            
        }

        return num == sum;
        
        
    }
    
    
}
