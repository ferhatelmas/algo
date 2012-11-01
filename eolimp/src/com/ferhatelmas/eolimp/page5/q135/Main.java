package com.ferhatelmas.eolimp.page5.q135;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    HashMap<Integer, Integer> factors = new HashMap<Integer, Integer>();

    while(n-- > 0) {
      int p = in.nextInt();
      for(int i=2; i<=p; i++) {
        int cnt = 0;
        while(p%i == 0) {
          cnt++;
          p /= i;
        }
        if(cnt > 0)
          if(factors.containsKey(i)) factors.put(i, Math.max(factors.get(i), cnt));
          else factors.put(i, cnt);
      }
    }

    BigInteger lcm = BigInteger.ONE;
    for(int factor : factors.keySet())
      lcm = lcm.multiply(new BigInteger(String.valueOf((int)Math.pow(factor, factors.get(factor)))));

    System.out.println(lcm);
  }

}
