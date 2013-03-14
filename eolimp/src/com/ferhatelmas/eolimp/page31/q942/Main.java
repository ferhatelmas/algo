package com.ferhatelmas.eolimp.page31.q942;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double[][] d = new double[4][2];

    for(int i=0; i<d.length; i++)
      for(int j=0; j<d[0].length; j++)
        d[i][j] = in.nextDouble();

    System.out.format(Locale.US, "%.3f %.3f\n%.3f %.3f\n",
        (d[0][0]+d[2][0])/2, (d[0][1]+d[2][1])/2,
        getLength(d, 0), getLength(d, 1));
  }

  private static double getLength(double[][] d, int k) {
    return Math.sqrt(Math.pow(d[k][0]-d[k+2][0], 2) +
        Math.pow(d[k][1]-d[k+2][1], 2));
  }
}
