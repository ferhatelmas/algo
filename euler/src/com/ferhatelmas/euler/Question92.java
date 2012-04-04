package com.ferhatelmas.euler;

public class Question92 {

    public static void main(String[] args) {

        int cnt = 0;
        
        for(int i=1; i<10000000; i++) {
            
            if(getChainNumber(i) == 89) cnt++;
            
        }
        System.out.println(cnt);
    }
    
    private static int getChainNumber(int i) {
        
        int val = getValue(i);
        while(val != 1 && val != 89) {
            val = getValue(val);
        }
        
        return val;
    }
    
    private static int getValue(int num) {
        
        String s = String.valueOf(num);
        
        int sum = 0;
        for(int i=0; i<s.length(); i++) {
            
            sum += (s.charAt(i)-'0') * (s.charAt(i)-'0');
            
        }

        return sum;
        
    }

}
