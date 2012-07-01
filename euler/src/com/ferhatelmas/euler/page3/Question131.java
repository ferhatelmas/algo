package com.ferhatelmas.euler.page3;

import java.util.Arrays;

public class Question131 {

  public static void main(String[] args) {

    boolean[] sieve = new boolean[1000001];
    Arrays.fill(sieve, true);

    for(int i=2; i<sieve.length; i++) {
      if(sieve[i]) {
        for(int j=2*i; j<sieve.length; j+=i) {
          sieve[j] = false;
        }
      }
    }

    long i = 1, j = 2;
    int cnt = 0, diff = (int)(j*j*j - i*i*i);
    while(diff < 1000000) {
      if(sieve[diff]) cnt++;
      i++;
      j++;
      diff = (int)(j*j*j - i*i*i);
    }

    System.out.println(cnt);
  }

}
