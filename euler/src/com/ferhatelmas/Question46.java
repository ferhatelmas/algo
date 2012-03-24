package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/8/12
 * Time: 6:23 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question46 {

    public static void main(String[] args) {

        int i=1;

        while(true) {

            if(i%2 == 1 && !isPrime(i)) {
                
                boolean flag = true;

                int j=1;
                while(true) {

                    int sub = i - 2*j*j;
                    if(sub < 2) {
                        flag = false;
                        break;
                    }
                    if(isPrime(sub)) break;
                    j++;
                }

                if(!flag) break;

            }

            i++;

        }

        System.out.println(i);

    }
    
    private static boolean isPrime(int n) {
        
        for(int i=2; i<=Math.sqrt(n); i++) {
            
            if(n%i == 0) return false;
            
        }
        
        return true;
        
    }

}
