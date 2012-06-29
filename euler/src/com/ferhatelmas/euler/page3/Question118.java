package com.ferhatelmas.euler.page3;

import java.util.Arrays;
import java.util.HashSet;

public class Question118 {

  private static HashSet<HashSet<Integer>> sets = new HashSet<HashSet<Integer>>();
  private static boolean[] primes = new boolean[987654322];

  public static void main(String[] args) {

    fillPrimes();

    permAndCountSets("123456789");
    System.out.println(sets.size());

  }

  private static void fillPrimes() {
    Arrays.fill(primes, true);

    primes[0] = false; primes[1] = false;
    for(int i=2; i<primes.length; i++) {
      if(primes[i]) {
        for(int j=2*i; j<primes.length; j+=i) {
          primes[j] = false;
        }
      }
    }
  }

  private static void permAndCountSets(String s) { permAndCountSets("", s); }
  private static void permAndCountSets(String prefix, String s) {
    int N = s.length();
    if (N == 0) {
      getPrimeSets(prefix, new HashSet<Integer>());
      return;
    }

    for (int i=0; i<N; i++) {
      permAndCountSets(prefix + s.charAt(i), s.substring(0, i) + s.substring(i+1, N));
    }

  }

  private static void getPrimeSets(String s, HashSet<Integer> set) {

    if(s.length() == 0) {
      HashSet<Integer> newSet = new HashSet<Integer>();
      for(int i : set) newSet.add(i);
      sets.add(newSet);
      return;
    }

    for(int i=0; i<s.length(); i++) {
      int num = Integer.parseInt(s.substring(0, i+1));
      if(primes[num]) {
        set.add(num);
        getPrimeSets(s.substring(i + 1), set);
        set.remove(num);
      }
    }

  }

}
