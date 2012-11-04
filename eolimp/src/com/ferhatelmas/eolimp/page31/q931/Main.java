package com.ferhatelmas.eolimp.page31.q931;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int sum = 0, mul = 1;
    for(char c : new Scanner(System.in).nextLine().toCharArray()) {
      int n = c - '0';
      sum += n;
      mul *= n;
    }
    Locale.setDefault(Locale.US);
    System.out.format("%.3f\n", mul/(double)sum);
  }

}
