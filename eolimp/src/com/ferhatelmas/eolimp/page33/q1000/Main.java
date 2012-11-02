package com.ferhatelmas.eolimp.page33.q1000;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while(in.hasNextInt())
      System.out.println(in.nextInt() + in.nextInt());
  }

}