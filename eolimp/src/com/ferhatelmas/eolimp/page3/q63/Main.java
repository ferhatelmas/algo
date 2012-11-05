package com.ferhatelmas.eolimp.page3.q63;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long m = in.nextLong(), n = in.nextLong();
    System.out.println(m * n - m - n + 2);
  }

}
