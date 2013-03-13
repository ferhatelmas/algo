package com.ferhatelmas.eolimp.page31.q934;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner in = new Scanner(System.in);
    double a = in.nextDouble(), b = in.nextDouble(), c = in.nextDouble();

    double s = (a + b + c) / 2;
    double t = 2 * Math.sqrt(s * (s-a) * (s-b) * (s-c));
    System.out.format("%.2f %.2f %.2f\n", t/a, t/b, t/c);
  }
}
