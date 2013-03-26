package com.ferhatelmas.eolimp.page40.q1210;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n = in.nextInt(), a = in.nextInt(), pow = 1, sum = 0;

    if(a == 1) {
      System.out.println(n*(n+1)/2);
      return;
    }

    for(int i=1; i<=n; i++) {
      pow *= a;
      sum += i*pow;
    }
    System.out.println(sum);
  }
}
