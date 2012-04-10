package com.ferhatelmas.euler.page1;

import java.util.ArrayList;
import java.util.List;

public class Question50 {

    public static void main(String[] args) {

        List<Integer> primes = new ArrayList<Integer>();

        int sum = 0;

        for(int i=2; i<1000000; i++) {

            if(isPrime(i)) {
                if(sum >= 1000000) break;
                sum += i;
                primes.add(sum);
            }

        }

        int max = 0, prime = -1;
        
        for(int i=0; i<primes.size(); i++) {

            for(int j=i-1; j>=0; j--) {

                if(isPrime(primes.get(i) - primes.get(j)) && i-j>max) {

                    max = i-j;
                    prime = primes.get(i) - primes.get(j);

                }

            }

        }

        System.out.println(prime);
        System.out.println(max);

    }

    private static boolean isPrime(int n) {

        for(int i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }

}
