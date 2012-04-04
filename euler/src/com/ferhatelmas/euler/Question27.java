package com.ferhatelmas.euler;

public class Question27 {

    public static void main(String[] args) {

        int max = 0, a = 0, b = 0;

        for(int i=-999; i<1000; i++) {

            for(int j=-999; j<1000; j++) {

                boolean flag = false;
                int n = 0, cnt = 0;

                while(true) {

                    int val = n*n+i*n+j;

                    if(!isPrime(val)) {
                        if(cnt > 0) flag = true;
                        break;
                    } else cnt++;

                    n++;

                }
                
                if(flag && cnt > max) {
                    max = cnt;
                    a = i;
                    b = j;
                } 

            }

        }

        System.out.println(a + " " + b + " " + a*b + " " + max);

    }
    
    private static boolean isPrime(int n) {

        
        if(n < 2) return false;

        for(int i=2; i<n/2+1; i++) {

            if(n%i == 0) return false;

        }

        return true;
    }
    

}
