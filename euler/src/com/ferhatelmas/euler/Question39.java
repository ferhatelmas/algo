package com.ferhatelmas.euler;

public class Question39 {

    public static void main(String[] args) {

        int max = Integer.MIN_VALUE, maxVal = 12;
        for(int i=12; i<1000; i++) {

            int cnt = getSolutions(i);
            if(cnt > max) {
                max = cnt;
                maxVal = i;
            }

        }

        System.out.println(maxVal);
        System.out.println(max);
        
    }
    
    private static int getSolutions(int p) {

        int cnt = 0;
        for(int i=0; i<p; i++) {

            for(int j=0; j<i; j++) {

                if((p-i-j)*(p-i-j) == (i*i+j*j)) cnt++;

            }

        }

        return cnt;
    }
    
}
