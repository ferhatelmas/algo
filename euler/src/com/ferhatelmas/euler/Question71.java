package com.ferhatelmas.euler;

public class Question71 {

    public static void main(String[] args) {

        final long a = 3;
        final long b = 7;
        long c = 0, d = 1;

        for (int i = 1000000; i>2; i--) {
            long j = (a * i - 1) / b;
            if (j * d > c * i) {
                d = i;
                c = j;
            }
        }
        System.out.println(c + " / " + d);
    }

}
