package com.ferhatelmas.euler.page3;

import java.math.BigInteger;
import java.util.HashSet;

public class Question146 {

  public static void main(String[] args) {

    HashSet<Integer> index = new HashSet<Integer>();
    index.add(2);index.add(6);index.add(8);index.add(12);index.add(26);

    long sum = 0;
    for(int i=10; i<150000000; i+=10) {

      if(i%3 == 0 || i%7 == 0 || i%13 == 0) continue;

      long val = (long)i*i+1;
      if(!new BigInteger(String.valueOf(val)).isProbablePrime(10)) continue;

      for(int j=1; j<27; j++) {
        boolean isPrime = new BigInteger(String.valueOf(val+j)).isProbablePrime(10);
        if((isPrime && !index.contains(j)) || (!isPrime && index.contains(j))) break;
        if(isPrime && j == 26) sum += i;
      }

    }

    System.out.println(sum);
  }
}
