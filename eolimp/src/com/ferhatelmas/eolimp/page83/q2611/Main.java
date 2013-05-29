package com.ferhatelmas.eolimp.page83.q2611;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String num = in.next(),
             a = in.next(), b = in.next(),
             s = num.replace(a, b);
    try {
      System.out.println(Integer.parseInt(s));
    } catch(NumberFormatException e) {
      System.out.println(s);
    }
  }
}
