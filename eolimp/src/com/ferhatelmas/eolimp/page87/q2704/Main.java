package com.ferhatelmas.eolimp.page87.q2704;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    StringBuilder sb = new StringBuilder();
    for(; n >= 100; n-=100) sb.append("C");
    for(n=addIrregular(sb, 10, "X", "L", "C", n); n >= 10; n-=10) sb.append("X");
    for(n=addIrregular(sb, 1, "I", "V", "X", n); n >= 1; n--) sb.append("I");
    System.out.println(sb.toString());
  }

  private static int addIrregular(StringBuilder sb, int pow, String l, String m, String h, int n) {
    if(n >= 9 * pow) {
      sb.append(l).append(h);
      n -= 9 * pow;
    } else if(n >= 5 * pow) {
      sb.append(m);
      n -= 5 * pow;
    } else if(n >= 4 * pow) {
      sb.append(l).append(m);
      n -= 4 * pow;
    }
    return n;
  }
}
