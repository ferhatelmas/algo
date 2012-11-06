package com.ferhatelmas.eolimp.page40.q1206;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(f91(n));
  }

  private static int f91(int n) {
    return n <= 100 ? f91(f91(n+11)) : n-10;
  }

}