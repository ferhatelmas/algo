package com.ferhatelmas.eolimp.page2.q57;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int x1 = in.nextInt(), y1 = in.nextInt();
    int x2 = in.nextInt(), y2 = in.nextInt(), z = in.nextInt();

    Locale.setDefault(Locale.US);
    System.out.format("%.3f\n", 1/Math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) + z * z));

  }

}
