package com.ferhatelmas;

public class Question44 {

    public static void main(String[] args) {

        for(int i=1; ;i++) {

            int n = i * (3 * i - 1) / 2;
            for(int j=i-1; j>0; j--) {
                
                int m = j * (3 * j -1) / 2;
                
                if(isPentagonal(n-m) && isPentagonal(n+m)) {

                    System.out.println(n-m);
                    System.exit(0);
                    
                }
            }

        }

    }


    private static boolean isPentagonal(int n) {

        double test = (Math.sqrt(24 * n + 1) + 1) / 6;

        return ((int)test) == test;

    }
    
}
