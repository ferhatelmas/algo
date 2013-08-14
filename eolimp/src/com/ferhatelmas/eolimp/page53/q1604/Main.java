package com.ferhatelmas.eolimp.page53.q1604;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    long mul = -1;
    for(char c : new Scanner(System.in).next().toCharArray())
      if((c - '0') % 2 == 0)
        mul = (c - '0') * (mul == -1 ? 1 : mul);
    System.out.println(mul);
  }
}
