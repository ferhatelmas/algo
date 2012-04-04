package com.ferhatelmas.euler;

public class Question21 {

    public static void main(String[] args) {

        int sum = 0;

        for(int i=1; i<=10000; i++) {

            int div = 0;

            for(int j=1; j<i; j++) {

                if(i%j == 0) div += j;

            }

            int div2 = 0;

            for(int j=1; j<div; j++) {

                if(div%j == 0) div2 += j;

            }

            if(div != div2 && div2 == i) {
                sum += i;
            }

        }

        System.out.println(sum);

    }

}
