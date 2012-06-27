package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Question87 {

  public static void main(String[] args) {

    boolean[] primes = new boolean[7072];
    Arrays.fill(primes, true);

    ArrayList<Long> squarePowers = new ArrayList<Long>();
    ArrayList<Long> cubePowers = new ArrayList<Long>();
    ArrayList<Long> fourthPowers = new ArrayList<Long>();

    for(int i=2; i<primes.length; i++) {
      if(primes[i]) {

        long t = i*i;
        squarePowers.add(t);
        t *= i;
        cubePowers.add(t);
        t *= i;
        fourthPowers.add(t);

        for(int j=2*i; j<primes.length; j+=i) {
          primes[j] = false;
        }
      }
    }

    HashSet<Long> numbers = new HashSet<Long>();
    for(long square : squarePowers) {
      for(long cube : cubePowers) {
        for(long fourth : fourthPowers) {
          long number = square + cube + fourth;
          if(number > 50000000) break;
          numbers.add(number);
        }
      }
    }

    System.out.println(numbers.size());
  }

}
