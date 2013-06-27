package com.ferhatelmas.eolimp.page86.q2713;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    long a = 1, b = 1;

    StringBuilder sb = new StringBuilder().append(1).append(1);
    while(true) {
      long temp = a;
      a += b;
      b = temp;
      sb.append(a);
      if(sb.length() >= n) {
        System.out.println(sb.charAt(n-1));
        break;
      }
    }
  }
}
