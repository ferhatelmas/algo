package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.List;

public class Question60 {

    public static void main(String[] args) {

        List<Integer> primes = new ArrayList<Integer>();

        for(int i=2; i<10000; i++) {

            if(isPrime(i)) primes.add(i);

        }

        boolean[][] gens = new boolean[primes.size()][primes.size()];

        for(int i=0; i<primes.size(); i++) {

            for(int j=0; j<primes.size(); j++) {

                gens[i][j] = doesGenerate(primes, i, j);

            }

        }

        System.out.println(chooseIndices(primes, gens));

    }

    private static int chooseIndices(List<Integer> primes, boolean[][] gens) {

        int sum = 0;

        for(int i=0; i<primes.size(); i++) {

            for(int j=i+1; j<primes.size(); j++) {
                
                if(gens[i][j]) {
                
                    for(int k=j+1; k<primes.size(); k++) {
                        
                        if(gens[i][k] && gens[j][k]) {
                        
                            for(int l=k+1; l<primes.size(); l++) {

                                if(gens[i][l] && gens[j][l] && gens[k][l]) {

                                    for(int m=l+1; m<primes.size(); m++) {

                                        if(gens[i][m] && gens[j][m] && gens[k][m] && gens[l][m]) {

                                            sum = primes.get(i);
                                            sum += primes.get(j);
                                            sum += primes.get(k);
                                            sum += primes.get(l);
                                            sum += primes.get(m);

                                            return sum;

                                        }
                                    }
                                }
                            }
                        }

                    }
                }
                        
            }

        }

        return sum;
        
    }
    
    private static boolean doesGenerate(List<Integer> primes, int i, int j) {
        
        return isPrime(Long.parseLong(String.valueOf(primes.get(i)).concat(String.valueOf(primes.get(j)))))
                && isPrime(Long.parseLong(String.valueOf(primes.get(j)).concat(String.valueOf(primes.get(i)))));
        
        
    }

    private static boolean isPrime(long n) {

        for(long i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }


}
