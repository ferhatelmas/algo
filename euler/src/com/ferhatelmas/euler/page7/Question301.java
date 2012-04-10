package com.ferhatelmas.euler.page7;

public class Question301 {

    public static void main(String[] args) {

        int cnt = 0;
        for(int i=1; i<=(1<<30); i++) {
            if((i^(2*i)^(3*i)) == 0) cnt++;
        }

        System.out.println(cnt);
    }
}
