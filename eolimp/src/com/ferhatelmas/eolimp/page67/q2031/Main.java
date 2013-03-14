package com.ferhatelmas.eolimp.page67.q2031;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt()-2;
    int a = 1, b = 1;

    System.out.println(1);
    while(n-- >= 0) {
      System.out.println(a);
      int t = a;
      a += b;
      b = t;
    }
  }
}
