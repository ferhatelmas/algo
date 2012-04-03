package com.ferhatelmas;

public class Question58 {

    public static void main(String[] args) {

        int side = 3;
        int total = 8;
        int prime = 5;
        int increment = 4;
        int last = 25;

        while((((double)prime) / total) >= 0.1) {

            side += 2;

            total += 4;

            increment += 2;

            for(int i=0; i<4; i++) {

                last += increment;
                if(isPrime(last)) prime++;

            }

        }

        System.out.println(side);

    }


    private static boolean isPrime(int n) {

        for(int i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }
}
