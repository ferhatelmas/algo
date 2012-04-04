package com.ferhatelmas.euler;

public class Question6 {

    public static void main(String[] args) {

        long sum = 0;
        for(int i=1; i<=100; i++) {
            sum += i*i;
        }
        System.out.println(5050*5050-sum);

    }

}
