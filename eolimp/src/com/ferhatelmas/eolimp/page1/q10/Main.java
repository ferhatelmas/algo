package com.ferhatelmas.eolimp.page1.q10;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    double d = new Scanner(System.in).nextInt(), sum = 0;

    int i=0;
    while(true) {
      sum += 1/(d-i);
      if(sum > 0.5) break;
      else i++;
    }

    System.out.println((int)(d-i));
  }

}