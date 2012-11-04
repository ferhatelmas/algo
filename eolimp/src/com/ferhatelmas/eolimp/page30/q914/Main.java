package com.ferhatelmas.eolimp.page30.q914;

import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.Locale;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    in.useLocale(Locale.US);

    int n = in.nextInt();
    double d, max = in.nextDouble();

    for(int i=1; i<n; i++) {
      d = in.nextDouble();
      if(d > max) max=d;
    }

    System.out.println(new DecimalFormat("#########0.00").format(Math.abs(max)).replace(",", "."));
  }

}