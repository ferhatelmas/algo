package com.ferhatelmas.euler.page8;

public class Question386 {

  public static void main(String[] args) {

    int primeFactorSieve[] = new int[100000001];
    int multiplesSieve[] = new int[primeFactorSieve.length];

    int sum = 1; // for 1
    for(int i=2; i<primeFactorSieve.length; i++) {
      if(primeFactorSieve[i] == 0) {
        sum++;  // handle primes
        for(int j=i; j<primeFactorSieve.length; j+=i) {
          primeFactorSieve[j] = i;
        }
      }
    }

    for(int i=2; i<primeFactorSieve.length; i++) {
      int n = i, count = 0;
      while(n > 1) {
        n /= primeFactorSieve[n];
        count++;
      }
      multiplesSieve[i] = count;
    }

    for(int i=2; i<multiplesSieve.length/2; i++) {
      for(int j=2*i; j<multiplesSieve.length; j+=i) {
        if(multiplesSieve[i] == multiplesSieve[j]/2) sum++;
      }
    }

    System.out.println(sum);
  }
}
