package com.ferhatelmas.eolimp.page85.q2667;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt(), x = in.nextInt(), y = in.nextInt();
    System.out.println(m * (x-1) + (x%2 == 1 ? y-1 : m-y));
  }
}
