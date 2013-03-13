package com.ferhatelmas.eolimp.page31.q944;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[][] points = new int[4][3];
    for(int i=0; i<points.length; i++)
      for(int j=0; j<points[0].length; j++)
        points[i][j] = in.nextInt();

    ArrayList<Double> sides = new ArrayList<Double>();
    for(int i=0; i<points.length; i++) {
      for(int j=i+1; j<points.length; j++) {
        double d = 0;
        for(int k=0; k<points[0].length; k++) {
          d += (points[i][k] - points[j][k]) * (points[i][k] - points[j][k]);
        }
        sides.add(Math.sqrt(d));
      }
    }

    double area = 0;
    int[] index = {0, 1, 3, 1, 2, 5, 3, 4, 5, 0, 2, 4};
    for(int i=0; i<index.length-2; i+=3)
      area += getArea(sides.get(index[i]), sides.get(index[i+1]), sides.get(index[i+2]));

    System.out.format(Locale.US, "%.1f\n", area);
  }

  private static double getArea(double d1, double d2, double d3) {
    double s = (d1+d2+d3) / 2;
    return Math.sqrt(s * (s-d1) * (s-d2) * (s-d3));
  }

}
