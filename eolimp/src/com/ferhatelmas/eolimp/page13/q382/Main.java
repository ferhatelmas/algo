package com.ferhatelmas.eolimp.page13.q382;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt(), k = in.nextInt(), m = in.nextInt();

    while(n > 0) {
      if(n > 0 && n <= k) {
        k = n;
        n -= k;
      } else if(n > 0) {
        n -= k;
        k += m;
      }

    }
    System.out.println(k);
  }

}