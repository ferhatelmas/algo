package com.ferhatelmas.eolimp.page12.q357;

import java.util.Scanner;
import java.util.Locale;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);
    in.useLocale(Locale.US);

    double d, max = 0;
    while(in.hasNextDouble()) {
      d = in.nextDouble();
      if(d>max) max=d;
    }
    System.out.println(new DecimalFormat("#########0.00").format(max).replace(",", "."));
  }

}