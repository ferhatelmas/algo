package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/26/12
 * Time: 10:57 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question69 {

    public static void main(String[] args) {
        
        int max = 1;
        int i=2;
        
        while(true) {
            
            if(isPrime(i)) {
                if(max*i < 1000000) max *= i;
                else break;
            }
            i++;
            
        }
        
        System.out.println(max);
        
    }
    
    private static boolean isPrime(int n) {
        
        for(int i=2; i<=Math.sqrt(n); i++) {
            
            if(n%i == 0) return false;
            
        }
        
        return true;
        
    }
}
