package com.ferhatelmas.eolimp.page3.q76;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double[] x = new double[2], y = new double[3];
    for(int i=0; i<x.length; i++)
      x[i] = in.nextDouble();
    for(int i=0; i<y.length; i++)
      y[i] = in.nextDouble();
    Arrays.sort(x);
    Arrays.sort(y);
    System.out.println(x[0]-y[0] > 0.0001 && x[1]-y[1] > 0.0001 ? 1 : 0);
  }
}
