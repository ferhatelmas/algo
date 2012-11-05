package com.ferhatelmas.eolimp.page13.q381;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int b = in.nextInt(), n = in.nextInt(), i;
    double pow = Integer.MAX_VALUE, val;

    for(i=1; i<=b; i++) {
      val = Math.abs(Math.pow(i, n)-b);

      if(val < pow) pow = val;
      else break;
    }

    System.out.println(i-1);
  }

}