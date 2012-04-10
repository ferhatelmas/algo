package com.ferhatelmas.euler.page1;

import java.util.Arrays;

public class Question49 {

    public static void main(String[] args) {

        for(int i=1000; i<10000; i++) {

            for(int j=1; i+2*j<10000; j++) {

                if(isPermPrime(i, j)) {
                    System.out.println(i + "" + (i+j) + "" + (i+2*j));
                    break;
                }

            }

        }

    }
    
    private static boolean isPermPrime(int i, int j) {
        
        char[] s1 = String.valueOf(i).toCharArray();
        char[] s2 = String.valueOf(i+j).toCharArray();
        char[] s3 = String.valueOf(i+2*j).toCharArray();

        if(!(isPrime(i) && isPrime(i+j) && isPrime(i+2*j))) return false;

        Arrays.sort(s1);
        Arrays.sort(s2);
        Arrays.sort(s3);
        
        String ss1 = new String(s1);
        String ss2 = new String(s2);
        String ss3 = new String(s3);

        if(ss1.equals(ss2) && ss2.equals(ss3) ) return true;
        else return false;

    }

    private static boolean isPrime(int n) {

        for(int i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }

}
