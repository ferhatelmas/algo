package com.ferhatelmas.eolimp.page20.q597;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(getMax(n));
  }

  private static int getMax(int n) {
    String s = Integer.toString(n, 2);

    for(int i=0; i<s.length(); i++)
      n = Math.max(n, Integer.parseInt(s.substring(i) + s.substring(0, i), 2));
    return n;
  }
}
