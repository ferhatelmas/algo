package com.ferhatelmas.eolimp.page41.q1247;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while(in.hasNext()) {
      int n = in.nextInt();
      if(n == 0) break;

      System.out.println(n + " " + getLcmCardinality(n));
    }
  }

  private static int getLcmCardinality(int n) {
    int i = 2, cnt, mul = 1;
    while(i <= n) {
      cnt = 0;
      while(n%i == 0) {
        cnt++;
        n /= i;
      }
      mul *= (2*cnt+1);
      if(++i > 45000) {
        mul *= 3;
        break;
      }
    }
    return mul/2+1;
  }
}
