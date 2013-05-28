package com.ferhatelmas.eolimp.page85.q2666;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    for(int i=0; i<n; i++) {
      System.out.print(repeat("2", n-i-1));
      System.out.print(0);
      System.out.println(repeat("1", i));
    }
  }

  private static String repeat(String s, int n) {
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; i++) sb.append(s);
    return sb.toString();
  }
}
