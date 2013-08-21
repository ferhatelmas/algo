package com.ferhatelmas.eolimp.page70.q2131;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double x1 = in.nextDouble(), y1 = in.nextDouble(),
           x2 = in.nextDouble(), y2 = in.nextDouble();
    System.out.format(Locale.US, "%.6f\n", Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)));
  }
}
