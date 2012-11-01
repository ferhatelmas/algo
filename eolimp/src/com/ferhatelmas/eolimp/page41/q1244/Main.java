package com.ferhatelmas.eolimp.page41.q1244;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt();

    if(Math.max(a, b)%Math.min(a, b) != 0) System.out.println(0);
    else {
      HashMap<Integer, Integer> g = getPrimeFactors(a);
      HashMap<Integer, Integer> l = getPrimeFactors(b);

      for(int key : g.keySet())
        if(l.get(key) - g.get(key) == 0) l.remove(key);

      System.out.println((int)Math.pow(2, l.size()));
    }
  }

  private static HashMap<Integer, Integer> getPrimeFactors(int n) {
    HashMap<Integer, Integer> factors = new HashMap<Integer, Integer>();
    for(int i=2; i<=n; i++) {
      int cnt = 0;
      while(n%i == 0) {
        cnt++;
        n /= i;
      }
      if(cnt > 0) factors.put(i, cnt);
    }
    return factors;
  }

}
