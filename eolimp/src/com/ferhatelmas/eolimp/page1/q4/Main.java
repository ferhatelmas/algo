package com.ferhatelmas.eolimp.page1.q4;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double x1 = in.nextDouble(), y1 = in.nextDouble(), r1 = in.nextDouble(),
           x2 = in.nextDouble(), y2 = in.nextDouble(), r2 = in.nextDouble();

    if(isEqual(r1, 0) || isEqual(r2, 0)) {
      System.out.println(0);
    } else if(isEqual(x1, x2) && isEqual(y1, y2)) {
      System.out.println(isEqual(r1, r2) ? -1 : 0);
    } else {
      double diff = Math.sqrt(Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2));
      if(diff > r1+r2 || diff+r1 < r2 || diff+r2 < r1)
        System.out.println(0);
      else if(isEqual(diff, r1+r2) || isEqual(diff+r2, r1) || isEqual(diff+r1, r2))
        System.out.println(1);
      else
        System.out.println(2);
    }
  }

  private static boolean isEqual(double d1, double d2) {
    return Math.abs(d1-d2) < 0.00001;
  }
}
