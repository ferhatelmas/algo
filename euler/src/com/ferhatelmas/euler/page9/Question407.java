package com.ferhatelmas.euler.page9;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Question407 {

  public static void main(String[] args) {
    int[] m = new int[10000001];
    Arrays.fill(m, 1);

    ArrayList<HashSet<Integer>> divisors = new ArrayList<HashSet<Integer>>(m.length);
    for(int i=0; i<m.length; i++) divisors.add(new HashSet<Integer>());
    for(int i=2; i<m.length; i++) {
      for(int j=i; j<m.length; j+=i) divisors.get(j).add(i);
      for(int a : divisors.get(i))
        for(int b : divisors.get(i-1)) {
          int n = a * b;
          if(n > m.length) break;
          if(i < n) m[n] = i;
        }
    }

    long sum = 0;
    for(int i=2; i<m.length; i++) sum += m[i];
    System.out.println(sum);
  }
}