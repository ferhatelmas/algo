package com.ferhatelmas.euler.page8;

import java.util.Arrays;

public class Question381 {

  public static void main(String[] args) {

    boolean[] primes = new boolean[100000000];
    Arrays.fill(primes, true);

    long sum = 0;

    for(int i=2; i<primes.length; i++) {
      if(primes[i]) {
        if(i >= 5) {
          sum += getReciprocal(i);
        }
        for(int j=2*i; j<primes.length; j+=i) {
          primes[j] = false;
        }
      }
    }

    System.out.println(sum);
  }

  private static int getReciprocal(int p) {
    int x = 0, y = 1, z, t, a = p, b = 8%p;

    while(b != 0) {
      z = a % b;
      t = x - a / b * y;
      a = b;
      b = z;
      x = y;
      y = t;
    }
    x = x<0 ? p+x : x;
    return (int)(((long) (p-3) * x) %p);
  }

}
