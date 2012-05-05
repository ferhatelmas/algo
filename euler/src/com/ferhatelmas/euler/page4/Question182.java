package com.ferhatelmas.euler.page4;

public class Question182 {

    public static void main(String[] args) {

        int p = 1008, q = 3642, phi = p*q;
        long sum = 0;

        for(int e=3; e<phi; e+=4) {
            if(gcd(phi, e) == 1 && gcd(q, e-1) == 2 && gcd(p, e-1) == 2) {
                sum += e;
            }
        }

        System.out.println(sum);
    }

    private static int gcd(int x, int y) {
        while (y != 0) {
            int r = x % y;
            x = y;
            y = r;
        }
        return x;
    }
}
