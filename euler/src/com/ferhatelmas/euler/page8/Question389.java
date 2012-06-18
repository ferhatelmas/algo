package com.ferhatelmas.euler.page8;

public class Question389 {

  public static void main(String[] args) {

    double expectation = 1;
    double[] diceSides = new double[]{4, 6, 8, 12, 20};

    for(double side : diceSides) {
      expectation *= (side+1)/2;
    }

    System.out.format("%.4f", expectation*(expectation-1)/3);

  }

}
