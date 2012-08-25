package com.ferhatelmas.eolimp.page2.q43;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    double sum = 1/in.nextDouble();
    sum += 1/in.nextDouble();
    sum += 1/in.nextDouble();
    double s = in.nextInt() / (1-sum);

    if(Math.abs(s-Math.round(s)) < 0.0001) System.out.println(Math.round(s));
    else System.out.println(-1);
  }
}
