package com.ferhatelmas.euler.page2;

public class Question63 {

    public static void main(String[] args) {

        int n = 1;
        int pow = 0;
        int cnt = 0;

        while(pow < 10) {

            pow = (int)Math.ceil(Math.pow(10, (n-1)/(double)n));
            cnt += 10-pow;
            
            n++;

        }

        System.out.println(cnt);

    }
    
}
