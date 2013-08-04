package com.ferhatelmas.eolimp.page52.q1544;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n;
    while((n = in.nextLong()) != 0) System.out.println(getNs(n));
  }

  private static String getNs(long n) {
    StringBuilder sb = new StringBuilder();
    for(int i=9; i>=0; i--)
      if((n-i)%9 == 0)
        sb.append(((n-i)/9)*10 + i).append(" ");
    return sb.substring(0, sb.length()-1);
  }
}
