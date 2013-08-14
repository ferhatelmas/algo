package com.ferhatelmas.eolimp.page9.q266;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int r = new BigInteger(in.nextLine()).compareTo(new BigInteger(in.nextLine()));
    if(r < 0)
      System.out.println("<");
    else if(r == 0)
      System.out.println("=");
    else
      System.out.println(">");
  }
}
