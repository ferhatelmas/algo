package com.ferhatelmas.euler;

public class Question47 {

    public static void main(String[] args) {

        for(int i=2; ; i++) {

            if(getFactors(i)) {
                System.out.println(i);
                break;
            }

        }

    }
    
    private static boolean getFactors(int n) {
        
        int cnt1 = getFactorsCnt(n);
        
        if(cnt1 == 4) {
            int cnt2 = getFactorsCnt(n+1);
            if(cnt2 == 4) {
        
                int cnt3 = getFactorsCnt(n+2);
                if(cnt3 == 4) {
                    int cnt4 = getFactorsCnt(n+3);
                    return cnt4 == 4;
                } else return false;
            } else return false;
        } else return false;
    }
    
    private static int getFactorsCnt(int n) {
        
        int cnt = 0; 
        for(int i=2; i<=n/2; i++) {
            
            if(n%i == 0 && isPrime(i)) cnt++; 
            
        }
        
        return cnt;
        
    }

    private static boolean isPrime(int n) {

        for(int i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }

}
