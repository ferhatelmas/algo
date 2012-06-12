package com.ferhatelmas.euler.page7;

import java.util.HashSet;

public class Question347 {

  private static int limit = 10000000;

  public static void main(String[] args) {

    int[] primeSieve = new int[limit+1];
    int[] primeSieveCnt = new int[limit+1];

    for(int i=2; i<primeSieve.length; i++) {
      if(primeSieve[i] == 0) {
        for(int j=i; j<primeSieve.length; j+=i) {
          primeSieve[j] = primeSieve[j] == 0 ? i : primeSieve[j]*i;
          primeSieveCnt[j]++;
        }
      }
    }

    long sum = 0;
    HashSet<Integer> set = new HashSet<Integer>();
    for(int i=limit; i>2; i--) {
      if(primeSieveCnt[i] == 2 && !set.contains(primeSieve[i])) {
        set.add(primeSieve[i]);
        sum += i;
      }
    }

    System.out.println(sum);
  }

}
